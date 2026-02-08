"""
This module provides a high-level interface for building and modifying a knowledge graph in a Neo4j database.

The central component is the GraphBuilder class, which encapsulates a Neo4j driver
connection and offers methods to create various types of nodes (entities) and the
relationships between them. It is designed to be used by scripts that extract structured
information (like entities and relations) and need to persist them as a graph.
"""

import json
import logging
from typing import Any, Dict, List

from neo4j import GraphDatabase
from src.graph.schema import EntityType, RelationType

logger = logging.getLogger(__name__)


class GraphBuilder:
    """
    Manages the connection to a Neo4j database and provides methods to
    create nodes and relationships based on the defined Schema.
    """

    def __init__(self, uri: str, user: str, password: str) -> None:
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self) -> None:
        self.driver.close()

    def clear_graph(self) -> None:
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
            logger.info("Graph cleared")

    def _sanitize_attributes(self, attributes: Dict[str, Any]) -> Dict[str, Any]:
        """Ensures attributes are Neo4j compatible (primitives or JSON strings)."""
        if attributes is None:
            return {}
        if isinstance(attributes, str):
            return {"description": attributes}
        if not isinstance(attributes, dict):
            return {"value": str(attributes)}

        sanitized: Dict[str, Any] = {}
        for k, v in attributes.items():
            if isinstance(v, (str, int, float, bool)):
                sanitized[k] = v
            elif isinstance(v, list):
                if all(isinstance(x, (str, int, float, bool)) for x in v):
                    sanitized[k] = v
                else:
                    sanitized[k] = [str(x) for x in v]
            elif isinstance(v, dict):
                sanitized[k] = json.dumps(v)
            else:
                sanitized[k] = str(v)
        return sanitized

    def _generate_id(self, entity_type: str, name: str) -> str:
        """Generate deterministic ID: e.g. 'Deity:Agni'."""
        clean_name = name.strip().replace(" ", "_").lower()
        return f"{entity_type}:{clean_name}"

    def create_entity(
        self, name: str, entity_type: str, attributes: Dict[str, Any]
    ) -> str:
        """
        Generic method to create/merge an entity node.

        Args:
            name: Display name (e.g. "Agni")
            entity_type: Must be a valid EntityType value (e.g. "Deity")
            attributes: Property dictionary

        Returns:
            The generated ID of the node.
        """
        # Validate type
        if entity_type not in [e.value for e in EntityType]:
            # Fallback or error? Let's default to Concept if unknown, or just warn.
            logger.warning(
                f"Unknown entity type '{entity_type}', defaulting to Concept"
            )
            entity_type = EntityType.CONCEPT.value

        node_id = self._generate_id(entity_type, name)
        attributes = self._sanitize_attributes(attributes)
        attributes["name"] = name
        attributes["id"] = node_id

        # We use a dynamic label. Neo4j drivers usually require label to be static in Cypher or injected carefully.
        # But we can use template string since we validated it against Enum.

        query = f"""
        MERGE (n:`{entity_type}` {{id: $id}})
        SET n += $attributes
        """

        with self.driver.session() as session:
            session.run(query, id=node_id, attributes=attributes)
            logger.debug(f"Merged {entity_type}: {name} ({node_id})")

        return node_id

    def create_relationship(
        self, from_name: str, to_name: str, rel_type: str, attributes: Dict[str, Any]
    ) -> None:
        """
        Creates a relationship.
        Note: We try to match nodes by Name first, because extraction might not know the Type beforehand
        to generate the ID.
        Or better: The extraction output should provide types for from/to if possible.
        But EntityExtractor output structure puts relationships separate from entities.

        Strategy:
        1. Find any node with property name=$from_name.
        2. Find any node with property name=$to_name.
        3. Create rel.
        """
        attributes = self._sanitize_attributes(attributes)

        # Basic validation
        if not from_name or not to_name:
            return

        if rel_type not in [r.value for r in RelationType]:
            logger.warning(f"Unknown relation type '{rel_type}', using RELATED_TO")
            rel_type = RelationType.RELATED_TO.value

        query = f"""
        MATCH (a), (b)
        WHERE a.name = $from_name AND b.name = $to_name
        MERGE (a)-[r:`{rel_type}`]->(b)
        SET r += $attributes
        """

        with self.driver.session() as session:
            session.run(
                query, from_name=from_name, to_name=to_name, attributes=attributes
            )
            logger.debug(f"Merged Rel: {from_name} -> {to_name} ({rel_type})")

    def create_entities_batch(self, entities: List[Dict[str, Any]]) -> None:
        """
        Batch merge multiple entities.
        Args:
            entities: List of dicts with {'name': str, 'type': str, 'attributes': dict}
        """
        if not entities:
            return

        # Group by type to use efficient parameterized queries
        by_type: Dict[str, List[Dict[str, Any]]] = {}
        for ent in entities:
            etype = ent["type"]
            if etype not in [e.value for e in EntityType]:
                etype = EntityType.CONCEPT.value

            if etype not in by_type:
                by_type[etype] = []

            node_id = self._generate_id(etype, ent["name"])
            attrs = self._sanitize_attributes(ent.get("attributes", {}))
            attrs["name"] = ent["name"]
            attrs["id"] = node_id
            by_type[etype].append(attrs)

        with self.driver.session() as session:
            for etype, batch in by_type.items():
                query = f"""
                UNWIND $batch AS props
                MERGE (n:`{etype}` {{id: props.id}})
                SET n += props
                """
                session.run(query, batch=batch)
                logger.info(f"Batch Merged {len(batch)} nodes of type {etype}")

    def create_relationships_batch(self, relationships: List[Dict[str, Any]]) -> None:
        """
        Batch merge relationships.
        Args:
            relationships: List of dicts {'from': str, 'to': str, 'type': str, 'attributes': dict}
        """
        if not relationships:
            return

        # Sanitize and prepare
        prepared = []
        for rel in relationships:
            # Safety check for required keys
            if "from" not in rel or "to" not in rel:
                logger.warning(f"Skipping malformed relationship: {rel}")
                continue

            rtype = rel.get("type", RelationType.RELATED_TO.value)
            if rtype not in [r.value for r in RelationType]:
                rtype = RelationType.RELATED_TO.value

            cleaned = {
                "from": rel["from"],
                "to": rel["to"],
                "type": rtype,
                "props": self._sanitize_attributes(rel.get("attributes", {})),
            }
            if cleaned["from"] and cleaned["to"]:
                prepared.append(cleaned)

        if not prepared:
            return

        # We can't easily group by type for the UNWIND if the type is dynamic in the relationship itself
        # unless we use APOC. Without APOC, we must group by relationship type.

        by_type: Dict[str, List[Dict[str, Any]]] = {}
        for item in prepared:
            rtype = item["type"]
            if rtype not in by_type:
                by_type[rtype] = []
            by_type[rtype].append(item)

        with self.driver.session() as session:
            for rtype, batch in by_type.items():
                # We match by NAME as per original strategy.
                # Ideally matching by ID is safer but extraction gives names.
                # Optimized query using UNWIND
                query = f"""
                UNWIND $batch AS row
                MATCH (a), (b)
                WHERE a.name = row.from AND b.name = row.to
                MERGE (a)-[r:`{rtype}`]->(b)
                SET r += row.props
                """
                session.run(query, batch=batch)
                logger.info(f"Batch Merged {len(batch)} relationships of type {rtype}")

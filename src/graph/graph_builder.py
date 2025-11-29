"""
This module provides a high-level interface for building and modifying a knowledge graph in a Neo4j database.

The central component is the GraphBuilder class, which encapsulates a Neo4j driver
connection and offers methods to create various types of nodes (entities) and the
relationships between them. It is designed to be used by scripts that extract structured
information (like entities and relations) and need to persist them as a graph.
"""

from neo4j import GraphDatabase
from typing import Dict
import logging
import json

logger = logging.getLogger(__name__)


class GraphBuilder:
    """
    Manages the connection to a Neo4j database and provides methods to
    create nodes and relationships, effectively building a knowledge graph.

    This class handles the lifecycle of the Neo4j driver and provides
    transactional methods to ensure data integrity when modifying the graph.
    """

    def __init__(self, uri, user, password):
        """
        Initializes the GraphBuilder and connects to the Neo4j database.

        Args:
            uri (str): The connection URI for the Neo4j database (e.g., "bolt://localhost:7687").
            user (str): The username for authentication.
            password (str): The password for authentication.
        """
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        """Closes the connection to the Neo4j database."""
        self.driver.close()

    def clear_graph(self):
        """
        Deletes all nodes and relationships from the graph.
        Use with caution, as this is a destructive operation.
        """
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
            logger.info("Graph cleared")

    def _sanitize_attributes(self, attributes: Dict) -> Dict:
        """
        Ensures that all attribute values are of a type that can be stored in Neo4j.

        Neo4j properties must be simple types (string, number, boolean) or lists of
        simple types. This method recursively sanitizes a dictionary of attributes,
        converting complex types like nested dicts or objects into JSON strings.

        Args:
            attributes (Dict): A dictionary of attributes for a node or relationship.

        Returns:
            Dict: A sanitized dictionary with Neo4j-compatible attribute values.
        """
        if attributes is None:
            return {}
        if isinstance(attributes, str):
            # If attributes are just a string, treat it as a description.
            return {"description": attributes}
        if not isinstance(attributes, dict):
            # For any other non-dict type, convert to string.
            return {"value": str(attributes)}

        sanitized = {}
        for k, v in attributes.items():
            if isinstance(v, (str, int, float, bool)):
                # Primitive types are stored as is.
                sanitized[k] = v
            elif isinstance(v, list):
                # For lists, ensure all elements are also primitive.
                if all(isinstance(x, (str, int, float, bool)) for x in v):
                    sanitized[k] = v
                else:
                    # If the list contains complex types, convert each item to a string.
                    sanitized[k] = [str(x) for x in v]
            elif isinstance(v, dict):
                # Nested dictionaries are serialized to a JSON string.
                sanitized[k] = json.dumps(v)
            else:
                # Any other complex type is converted to its string representation.
                sanitized[k] = str(v)
        return sanitized

    def create_person(self, name: str, attributes: Dict):
        """
        Creates or updates a 'Person' node in the graph.

        If a Person node with the given name already exists, it will be updated
        with the new attributes. Otherwise, a new node will be created.

        Args:
            name (str): The unique name of the person.
            attributes (Dict): A dictionary of properties for the person.
        """
        attributes = self._sanitize_attributes(attributes)
        with self.driver.session() as session:
            session.run(
                """
                MERGE (p:Person {name: $name})
                SET p += $attributes
            """,
                name=name,
                attributes=attributes,
            )
            logger.debug(f"Created/Merged Person: {name}")

    def create_concept(self, name: str, attributes: Dict):
        """
        Creates or updates a 'Concept' node in the graph.

        Args:
            name (str): The unique name of the concept.
            attributes (Dict): A dictionary of properties for the concept.
        """
        attributes = self._sanitize_attributes(attributes)
        with self.driver.session() as session:
            session.run(
                """
                MERGE (c:Concept {name: $name})
                SET c += $attributes
            """,
                name=name,
                attributes=attributes,
            )
            logger.debug(f"Created/Merged Concept: {name}")

    def create_event(self, name: str, attributes: Dict):
        """
        Creates or updates an 'Event' node in the graph.

        Args:
            name (str): The unique name of the event.
            attributes (Dict): A dictionary of properties for the event.
        """
        attributes = self._sanitize_attributes(attributes)
        with self.driver.session() as session:
            session.run(
                """
                MERGE (e:Event {name: $name})
                SET e += $attributes
            """,
                name=name,
                attributes=attributes,
            )
            logger.debug(f"Created/Merged Event: {name}")

    def create_location(self, name: str, attributes: Dict):
        """
        Creates or updates a 'Location' node in the graph.

        Args:
            name (str): The unique name of the location.
            attributes (Dict): A dictionary of properties for the location.
        """
        attributes = self._sanitize_attributes(attributes)
        with self.driver.session() as session:
            session.run(
                """
                MERGE (l:Location {name: $name})
                SET l += $attributes
            """,
                name=name,
                attributes=attributes,
            )
            logger.debug(f"Created/Merged Location: {name}")

    def create_relationship(
        self, from_name: str, to_name: str, rel_type: str, attributes: Dict
    ):
        """
        Creates or updates a relationship between two nodes.

        The direction of the relationship is from the 'from_name' node to the
        'to_name' node. Nodes are matched by their 'name' property, regardless
        of their label (e.g., Person, Concept).

        Args:
            from_name (str): The name of the starting node.
            to_name (str): The name of the ending node.
            rel_type (str): The type of the relationship (e.g., "RELATED_TO").
            attributes (Dict): A dictionary of properties for the relationship.
        """
        attributes = self._sanitize_attributes(attributes)

        if not from_name or not to_name:
            logger.warning(
                "Skipping relationship creation due to missing start or end node name."
            )
            return

        # Avoid creating relationships from unstructured text extractions that may
        # contain arrows or other non-entity patterns.
        if "→" in from_name or "→" in to_name:
            logger.warning(
                f"Skipping relationship with arrow notation: {from_name} → {to_name}"
            )
            return

        with self.driver.session() as session:
            # This query finds two nodes, `a` and `b`, by their `name` property and
            # creates a relationship of `rel_type` between them.
            # `MERGE` ensures that the same relationship is not created multiple times.
            # `SET r += $attributes` updates the relationship's properties.
            # This assumes that node names are unique across the entire graph.
            session.run(
                f"""
                MATCH (a {{name: $from_name}})
                MATCH (b {{name: $to_name}})
                MERGE (a)-[r:{rel_type}]->(b)
                SET r += $attributes
            """,
                from_name=from_name,
                to_name=to_name,
                attributes=attributes,
            )
            logger.debug(
                f"Created/Merged Relationship: {from_name} -[{rel_type}]-> {to_name}"
            )

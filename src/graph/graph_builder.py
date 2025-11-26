from neo4j import GraphDatabase
from typing import Dict
import logging
import json

logger = logging.getLogger(__name__)

class GraphBuilder:
    """Build knowledge graph in Neo4j."""
    
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        
    def close(self):
        self.driver.close()

    def _sanitize_attributes(self, attributes):
        """Ensure attributes is a flat dictionary with valid Neo4j types."""
        if attributes is None:
            return {}
        if isinstance(attributes, str):
            return {"description": attributes}
        if not isinstance(attributes, dict):
            return {"value": str(attributes)}
            
        sanitized = {}
        for k, v in attributes.items():
            if isinstance(v, (str, int, float, bool)):
                sanitized[k] = v
            elif isinstance(v, list):
                # Check if list contains only primitives
                if all(isinstance(x, (str, int, float, bool)) for x in v):
                    sanitized[k] = v
                else:
                    sanitized[k] = [str(x) for x in v] # Convert complex list items to strings
            elif isinstance(v, dict):
                # Stringify nested dicts
                sanitized[k] = json.dumps(v)
            else:
                sanitized[k] = str(v)
        return sanitized
        
    def create_person(self, name: str, attributes: Dict):
        attributes = self._sanitize_attributes(attributes)
        with self.driver.session() as session:
            session.run("""
                MERGE (p:Person {name: $name})
                SET p += $attributes
            """, name=name, attributes=attributes)
            logger.debug(f"Created Person: {name}")
    
    def create_concept(self, name: str, attributes: Dict):
        attributes = self._sanitize_attributes(attributes)
        with self.driver.session() as session:
            session.run("""
                MERGE (c:Concept {name: $name})
                SET c += $attributes
            """, name=name, attributes=attributes)
            logger.debug(f"Created Concept: {name}")
            
    def create_event(self, name: str, attributes: Dict):
        attributes = self._sanitize_attributes(attributes)
        with self.driver.session() as session:
            session.run("""
                MERGE (e:Event {name: $name})
                SET e += $attributes
            """, name=name, attributes=attributes)
            logger.debug(f"Created Event: {name}")

    def create_location(self, name: str, attributes: Dict):
        attributes = self._sanitize_attributes(attributes)
        with self.driver.session() as session:
            session.run("""
                MERGE (l:Location {name: $name})
                SET l += $attributes
            """, name=name, attributes=attributes)
            logger.debug(f"Created Location: {name}")
    
    def create_relationship(self, from_name: str, to_name: str, 
                           rel_type: str, attributes: Dict):
        attributes = self._sanitize_attributes(attributes)
        with self.driver.session() as session:
            # Try to match nodes with any label, assuming names are unique across labels
            # Or we could be more specific if we knew the types of from/to nodes
            # For simplicity, we'll match on name property across all nodes
            # But it's better to be specific if possible. 
            # Given the extractor returns types, we might want to pass types in create_relationship
            # For now, let's assume names are unique enough or we match on any node.
            session.run(f"""
                MATCH (a {{name: $from_name}})
                MATCH (b {{name: $to_name}})
                MERGE (a)-[r:{rel_type}]->(b)
                SET r += $attributes
            """, from_name=from_name, to_name=to_name, attributes=attributes)
            logger.debug(f"Created Relationship: {from_name} -> {to_name} ({rel_type})")

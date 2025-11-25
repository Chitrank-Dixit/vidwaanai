from neo4j import GraphDatabase
from typing import Dict

class GraphBuilder:
    """Build knowledge graph in Neo4j."""
    
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        
    def close(self):
        self.driver.close()
        
    def create_person(self, name: str, attributes: Dict):
        with self.driver.session() as session:
            session.run("""
                MERGE (p:Person {name: $name})
                SET p += $attributes
            """, name=name, attributes=attributes)
    
    def create_concept(self, name: str, attributes: Dict):
        with self.driver.session() as session:
            session.run("""
                MERGE (c:Concept {name: $name})
                SET c += $attributes
            """, name=name, attributes=attributes)
            
    def create_event(self, name: str, attributes: Dict):
        with self.driver.session() as session:
            session.run("""
                MERGE (e:Event {name: $name})
                SET e += $attributes
            """, name=name, attributes=attributes)

    def create_location(self, name: str, attributes: Dict):
        with self.driver.session() as session:
            session.run("""
                MERGE (l:Location {name: $name})
                SET l += $attributes
            """, name=name, attributes=attributes)
    
    def create_relationship(self, from_name: str, to_name: str, 
                           rel_type: str, attributes: Dict):
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

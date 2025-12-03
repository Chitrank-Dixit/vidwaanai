from typing import List, Dict


class GraphRetriever:
    """Retrieve relevant subgraphs for queries."""

    def __init__(self, neo4j_driver):
        self.driver = neo4j_driver

    def find_teachings(
        self, person_name: str, concept_name: str, depth: int = 2
    ) -> List[Dict]:
        """Find all teachings by a person about a concept."""
        with self.driver.session() as session:
            result = session.run(
                f"""
                MATCH path = (p:Person {{name: $person}})-[:TEACHES*1..{depth}]->(c:Concept)
                WHERE c.name CONTAINS $concept OR c.sanskrit_term CONTAINS $concept
                RETURN path, 
                       [node in nodes(path) | properties(node)] as entities,
                       [rel in relationships(path) | properties(rel)] as relations
                LIMIT 20
            """,
                person=person_name,
                concept=concept_name,
            )

            return [record.data() for record in result]

    def find_related_concepts(self, concept_name: str, depth: int = 2):
        """Find concepts related to a given concept."""
        with self.driver.session() as session:
            result = session.run(
                f"""
                MATCH path = (c1:Concept {{name: $concept}})-[:RELATES_TO*1..{depth}]-(c2:Concept)
                RETURN c2.name as related_concept,
                       c2.definition as definition,
                       length(path) as distance
                ORDER BY distance
                LIMIT 10
            """,
                concept=concept_name,
            )

            return [record.data() for record in result]

    def find_person_connections(self, person1: str, person2: str, depth: int = 3):
        """Find how two persons are connected."""
        with self.driver.session() as session:
            result = session.run(
                f"""
                MATCH path = shortestPath((p1:Person {{name: $person1}})-[*..{depth}]-(p2:Person {{name: $person2}}))
                RETURN path,
                       [node in nodes(path) | properties(node)] as entities,
                       [rel in relationships(path) | properties(rel)] as relations
            """,
                person1=person1,
                person2=person2,
            )

            return [record.data() for record in result]

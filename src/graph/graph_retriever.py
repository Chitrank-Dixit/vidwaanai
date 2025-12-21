from typing import Any, Dict, List


class GraphRetriever:
    """Retrieve relevant subgraphs for queries."""

    def __init__(self, neo4j_driver: Any) -> None:
        self.driver = neo4j_driver

    def find_teachings(
        self, person_name: str, concept_name: str, depth: int = 2
    ) -> List[Dict[str, Any]]:
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

    def find_related_concepts(
        self, concept_name: str, depth: int = 2
    ) -> List[Dict[str, Any]]:
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

    def find_person_connections(
        self, person1: str, person2: str, depth: int = 3
    ) -> List[Dict[str, Any]]:
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

    def get_context_subgraph(
        self, entity_names: List[str], depth: int = 1
    ) -> List[Dict[str, Any]]:
        """
        Get 1-hop subgraph for a list of entities to provide RAG context.
        Returns a list of relationships formatted as strings or dicts.
        """
        if not entity_names:
            return []

        with self.driver.session() as session:
            # We match any node with a name in the list, and find immediate neighbors (any direction)
            result = session.run(
                """
                MATCH (a)-[r]-(b)
                WHERE a.name IN $names
                RETURN a.name as source, 
                       type(r) as relation, 
                       b.name as target,
                       labels(a) as source_type,
                       labels(b) as target_type
                LIMIT 20
                """,
                names=entity_names
            )
            return [record.data() for record in result]

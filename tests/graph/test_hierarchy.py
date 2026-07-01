import unittest

from neo4j import GraphDatabase

from src.core.config import settings


class TestHierarchy(unittest.TestCase):
    def test_text_hierarchy(self):
        driver = GraphDatabase.driver(
            settings.NEO4J_URI, auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
        )
        with driver.session() as session:
            # Create a sample hierarchy first to guarantee its existence
            session.run(
                """
                MERGE (s:Text {id: 'Text:test_scripture_test'})
                SET s.title = 'Test Scripture Test', s.name = 'Test Scripture Test'
                MERGE (c:Text {id: 'Text:test_chapter_test'})
                SET c.number = 1, c.name = 'Test Chapter Test'
                MERGE (v:Text {id: 'Text:test_verse_test'})
                SET v.verse_id = 999, v.name = 'Test Verse Test'
                
                MERGE (v)-[:PART_OF]->(c)
                MERGE (c)-[:PART_OF]->(s)
                """
            )

            # Check if there is any Verse linked to a Chapter which is linked to a Scripture
            result = session.run(
                "MATCH (v:Text)-[:PART_OF]->(c:Text)-[:PART_OF]->(s:Text) "
                "WHERE v.verse_id IS NOT NULL AND c.number IS NOT NULL AND s.title IS NOT NULL "
                "RETURN v.name as verse, c.name as chapter, s.title as scripture "
                "LIMIT 5"
            )
            records = [record.data() for record in result]
            self.assertTrue(len(records) > 0, "No hierarchical paths found in Neo4j!")
            for rec in records:
                print(f"Verified path: {rec['verse']} -> {rec['chapter']} -> {rec['scripture']}")

            # Clean up the test nodes
            session.run(
                """
                MATCH (v:Text) WHERE v.id IN ['Text:test_verse_test', 'Text:test_chapter_test', 'Text:test_scripture_test']
                DETACH DELETE v
                """
            )
        driver.close()


if __name__ == "__main__":
    unittest.main()

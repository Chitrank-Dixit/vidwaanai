import pytest
from src.graph.graph_builder import GraphBuilder

# Mark as integration test
pytestmark = pytest.mark.integration


class TestGraphOperations:
    @pytest.fixture(scope="class")
    def graph_builder(self):
        # Use test Neo4j URI from settings
        from src.core.config import settings

        uri = settings.NEO4J_URI
        user = settings.NEO4J_USER
        password = settings.NEO4J_PASSWORD

        builder = GraphBuilder(uri, user, password)
        yield builder
        builder.close()

    @pytest.fixture(autouse=True)
    def clean_graph(self, graph_builder):
        """Clean graph before each test."""
        graph_builder.clear_graph()
        yield
        # Optional: clean after
        # graph_builder.clear_graph()

    def test_create_person(self, graph_builder):
        """Test creating a person node."""
        name = "Arjuna"
        attributes = {"role": "Warrior", "description": "Pandava prince"}

        graph_builder.create_person(name, attributes)

        # Verify
        with graph_builder.driver.session() as session:
            result = session.run("MATCH (p:Person {name: $name}) RETURN p", name=name)
            record = result.single()
            assert record is not None
            node = record["p"]
            assert node["name"] == name
            assert node["role"] == "Warrior"

    def test_create_relationship(self, graph_builder):
        """Test creating relationship between nodes."""
        # Create nodes first
        graph_builder.create_person("Krishna", {"role": "God"})
        graph_builder.create_person("Arjuna", {"role": "Warrior"})

        # Create relationship
        graph_builder.create_relationship(
            "Krishna", "Arjuna", "TEACHES", {"context": "Gita"}
        )

        # Verify
        with graph_builder.driver.session() as session:
            result = session.run(
                """
                MATCH (a:Person {name: 'Krishna'})-[r:TEACHES]->(b:Person {name: 'Arjuna'})
                RETURN r
                """
            )
            record = result.single()
            assert record is not None
            rel = record["r"]
            assert rel["context"] == "Gita"

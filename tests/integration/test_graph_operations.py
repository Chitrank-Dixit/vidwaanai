import pytest
from typing import Generator
from src.graph.graph_builder import GraphBuilder

# Mark as integration test
pytestmark = pytest.mark.integration


class TestGraphOperations:
    @pytest.fixture(scope="class")
    def graph_builder(self) -> Generator[GraphBuilder, None, None]:
        # Use test Neo4j URI from settings
        from src.core.config import settings

        uri = settings.NEO4J_URI
        user = settings.NEO4J_USER
        password = settings.NEO4J_PASSWORD

        builder = GraphBuilder(uri, user, password)
        yield builder
        builder.close()

    @pytest.fixture(autouse=True)
    def clean_graph(self, graph_builder: GraphBuilder) -> Generator[None, None, None]:
        """Clean graph before each test."""
        graph_builder.clear_graph()
        yield
        # Optional: clean after
        # graph_builder.clear_graph()

    def test_create_person(self, graph_builder: GraphBuilder) -> None:
        """Test creating a person node."""
        name = "Arjuna"
        attributes = {"role": "Warrior", "description": "Pandava prince"}

        graph_builder.create_entity(name, "Character", attributes)

        # Verify
        with graph_builder.driver.session() as session:
            result = session.run("MATCH (p:Character {name: $name}) RETURN p", name=name)
            record = result.single()
            assert record is not None
            node = record["p"]
            assert node["name"] == name
            assert node["role"] == "Warrior"

    def test_create_relationship(self, graph_builder: GraphBuilder) -> None:
        """Test creating relationship between nodes."""
        # Create nodes first
        graph_builder.create_entity("Krishna", "Character", {"role": "God"})
        graph_builder.create_entity("Arjuna", "Character", {"role": "Warrior"})

        # Create relationship
        graph_builder.create_relationship(
            "Krishna", "Arjuna", "TEACHER_OF", {"context": "Gita"}
        )

        # Verify
        with graph_builder.driver.session() as session:
            result = session.run(
                """
                MATCH (a:Character {name: 'Krishna'})-[r:TEACHER_OF]->(b:Character {name: 'Arjuna'})
                RETURN r
                """
            )
            record = result.single()
            assert record is not None
            rel = record["r"]
            assert rel["context"] == "Gita"

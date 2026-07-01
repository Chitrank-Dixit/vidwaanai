import unittest
from unittest.mock import MagicMock

from src.graph.graph_builder import GraphBuilder


class TestAliasResolution(unittest.TestCase):
    def setUp(self):
        self.mock_driver = MagicMock()
        self.session = MagicMock()
        self.mock_driver.session.return_value.__enter__.return_value = self.session

    def test_create_entity_with_aliases(self):
        builder = GraphBuilder("bolt://localhost:7687", "neo4j", "password")
        builder.driver = self.mock_driver

        # Call create_entity with aliases attribute
        builder.create_entity(
            "Arjuna", "Character", {"role": "hero", "aliases": ["Partha", "Dhananjaya"]}
        )

        # Verify session.run was called
        self.session.run.assert_called_once()
        args, kwargs = self.session.run.call_args

        # Verify the Cypher query contains the aliases merge statement
        query = args[0]
        self.assertIn("REDUCE", query)
        self.assertIn("n.aliases = REDUCE", query)

        # Verify parameters passed to Cypher
        self.assertEqual(kwargs["id"], "Character:arjuna")
        self.assertEqual(kwargs["new_aliases"], ["Partha", "Dhananjaya"])
        self.assertEqual(kwargs["attributes"]["name"], "Arjuna")
        self.assertNotIn(
            "aliases", kwargs["attributes"]
        )  # should be popped from attributes


if __name__ == "__main__":
    unittest.main()

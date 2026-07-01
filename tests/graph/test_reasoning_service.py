import unittest
from unittest.mock import MagicMock

from src.graph.graph_manager import GraphManager
from src.graph.reasoning_service import GraphReasoningService


class TestGraphReasoningServiceUnit(unittest.TestCase):
    def setUp(self):
        self.mock_gm = MagicMock()
        self.service = GraphReasoningService(self.mock_gm)

    def test_get_entity_details(self):
        # Mock entity details
        self.mock_gm.execute_query.side_effect = [
            # Check if exists (returns properties dict)
            [{"entity": {"id": "Concept:dharma", "name": "Dharma"}}],
            # Neighbors details
            [
                {
                    "source": {"id": "Concept:dharma", "name": "Dharma"},
                    "rel_type": "RELATES_TO",
                    "rel_properties": {"context": "core philosophy"},
                    "target": {"id": "Concept:karma", "name": "Karma"},
                    "rel_id": "rel1",
                }
            ],
        ]

        details = self.service.get_entity_details("Concept:dharma")

        self.assertEqual(details["entity"]["name"], "Dharma")
        self.assertEqual(len(details["outgoing"]), 1)
        self.assertEqual(details["outgoing"][0]["type"], "RELATES_TO")
        self.assertEqual(details["outgoing"][0]["target"]["name"], "Karma")

    def test_find_shortest_path(self):
        self.mock_gm.execute_query.return_value = [
            {
                "path_nodes": [
                    {"id": "Character:rama", "name": "Rama"},
                    {"id": "Character:vishnu", "name": "Vishnu"},
                ],
                "path_rels": [
                    {
                        "type": "MANIFESTS_AS",
                        "start": "Rama",
                        "end": "Vishnu",
                        "properties": {},
                    }
                ],
                "len": 1.0,
            }
        ]

        path_res = self.service.find_shortest_path("Character:rama", "Character:vishnu")

        self.assertTrue(path_res["found"])
        self.assertEqual(path_res["length"], 1.0)
        self.assertEqual(path_res["nodes"][0]["name"], "Rama")
        self.assertEqual(path_res["relationships"][0]["type"], "MANIFESTS_AS")

    def test_search_entities(self):
        self.mock_gm.execute_query.return_value = [
            {"node": {"id": "Character:rama", "name": "Rama"}}
        ]

        nodes = self.service.search_entities("Rama")
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0]["name"], "Rama")

    def test_reason_about_entity(self):
        self.mock_gm.execute_query.return_value = [{"names": ["Rama", "Vishnu"]}]

        implications = self.service.reason_about_entity("Character:rama")
        self.assertEqual(len(implications["implications"]), 1)
        self.assertEqual(implications["implications"][0], "(Rama) -> (Vishnu)")

    def test_get_hierarchy(self):
        self.mock_gm.execute_query.side_effect = [
            [{"parent": {"id": "Deity:vishnu", "name": "Vishnu"}}],
            [{"child": {"id": "Character:rama", "name": "Rama"}}],
        ]

        hierarchy = self.service.get_hierarchy("Character:rama")
        self.assertEqual(len(hierarchy["parents"]), 1)
        self.assertEqual(hierarchy["parents"][0]["name"], "Vishnu")
        self.assertEqual(len(hierarchy["children"]), 1)
        self.assertEqual(hierarchy["children"][0]["name"], "Rama")


class TestGraphReasoningServiceIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            # Initialize real GraphManager
            cls.gm = GraphManager()
            cls.service = GraphReasoningService(cls.gm)
            cls.enabled = True
        except Exception as e:
            print(f"Skipping integration tests: Neo4j not available ({e})")
            cls.enabled = False

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, "gm") and cls.gm:
            cls.gm.close()

    def test_integration_shortest_path_rama_vishnu(self):
        if not self.enabled:
            self.skipTest("Neo4j database not running")

        res = self.service.find_shortest_path("Character:rama", "Character:vishnu")
        if res["found"]:
            self.assertTrue(res["length"] > 0)
            self.assertTrue(
                any(r["type"] == "MANIFESTS_AS" for r in res["relationships"])
            )
        else:
            # Fallback if DB is empty or has different records
            print("Rama to Vishnu path not found in active graph.")

    def test_integration_hierarchy_dharma(self):
        if not self.enabled:
            self.skipTest("Neo4j database not running")

        res_concept = self.service.get_hierarchy("Concept:dharma")
        self.assertIsNotNone(res_concept)
        self.assertTrue("parents" in res_concept)
        self.assertTrue("children" in res_concept)


if __name__ == "__main__":
    unittest.main()

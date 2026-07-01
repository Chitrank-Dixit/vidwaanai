import unittest
from unittest.mock import MagicMock, patch

from src.agent.vidwaan_agent import VidwaanAI


class TestAgentReasoning(unittest.TestCase):
    @patch("src.agent.vidwaan_agent.DatabaseManager")
    @patch("src.agent.vidwaan_agent.EmbeddingManager")
    @patch("src.agent.vidwaan_agent.MultilingualSearch")
    @patch("src.agent.vidwaan_agent.GraphDatabase")
    @patch("src.agent.vidwaan_agent.GraphManager")
    @patch("src.agent.vidwaan_agent.GraphReasoningService")
    def test_graph_rag_query_flow(
        self,
        mock_reasoning_svc,
        mock_graph_mgr,
        mock_graph_db,
        mock_multilingual_search,
        mock_embedding_mgr,
        mock_db_mgr,
    ):
        # Mock database verses returned
        mock_db_instance = mock_db_mgr.return_value
        mock_db_instance.get_all_verses.return_value = []
        mock_db_instance.retrieve_verses.return_value = [
            {
                "id": 1,
                "scripture": "Bhagavad Gita",
                "chapter": 2,
                "verse": 47,
                "text": "karmany evadhikaras te",
                "translation": "Duty text",
                "similarity": 0.9,
            }
        ]

        # Mock multilingual search output
        mock_multilingual_search.return_value.process_query.return_value = {
            "language_code": "en",
            "embedding": [0.1] * 1024,
        }

        # Mock reasoning service
        mock_svc_instance = mock_reasoning_svc.return_value
        mock_svc_instance.search_entities.side_effect = [
            [{"id": "Character:rama", "name": "Rama"}]
        ]
        mock_svc_instance.reason_about_entity.return_value = {
            "implications": ["(Rama) -[:MANIFESTS_AS]-> (Vishnu)"]
        }
        mock_svc_instance.get_hierarchy.return_value = {
            "parents": [{"id": "Deity:vishnu", "name": "Vishnu"}]
        }

        # Initialize agent
        agent = VidwaanAI(
            db_url="postgresql://localhost:5432/db",
            openai_key="key",
            use_lmstudio=False,
            enable_graph_rag=True,
            neo4j_uri="bolt://localhost:7687",
            neo4j_user="neo4j",
            neo4j_password="password",
        )

        # Mock LLM response
        agent.llm = MagicMock()
        agent.llm.generate.return_value = "This is a RAG answer."

        # Mock entity extractor
        agent.entity_extractor = MagicMock()
        agent.entity_extractor.extract_from_query.return_value = [
            {"name": "Rama", "type": "Person"}
        ]

        # Query
        res = agent.query("Who is Rama?")

        # Assertions
        self.assertIn("This is a RAG answer.", res["answer"])
        # Verify entity extraction was called
        agent.entity_extractor.extract_from_query.assert_called_with("Who is Rama?")
        # Verify reasoning service was called to search and reason
        mock_svc_instance.search_entities.assert_called_with("Rama", limit=1)
        mock_svc_instance.reason_about_entity.assert_called_with(
            "Character:rama", hops=2
        )
        mock_svc_instance.get_hierarchy.assert_called_with("Character:rama")


if __name__ == "__main__":
    unittest.main()

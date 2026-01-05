import pytest
from src.agent.vidwaan_agent import VidwaanAI
from src.db.db_manager import DatabaseManager
from src.graph.graph_builder import GraphBuilder
from unittest.mock import MagicMock, patch
from typing import Generator

# Mark as e2e test
pytestmark = pytest.mark.e2e


class TestCompleteQuery:
    @pytest.fixture(scope="class")
    def db_manager(self) -> DatabaseManager:
        from src.core.config import settings

        return DatabaseManager(settings.DATABASE_URL)

    @pytest.fixture(scope="class")
    def graph_builder(self) -> Generator[GraphBuilder, None, None]:
        from src.core.config import settings

        uri = settings.NEO4J_URI
        user = settings.NEO4J_USER
        password = settings.NEO4J_PASSWORD
        builder = GraphBuilder(uri, user, password)
        yield builder
        builder.close()

    @pytest.fixture(scope="class")
    def embedding_manager(self) -> MagicMock:
        # Mock embedding manager to return 1024 dim vectors
        manager = MagicMock()
        manager.embed_text.side_effect = lambda text: [0.1] * 1024
        manager.embed_batch.side_effect = lambda texts: [[0.1] * 1024 for _ in texts]
        return manager

    @pytest.fixture(autouse=True)
    def setup_system(
        self,
        db_manager: DatabaseManager,
        graph_builder: GraphBuilder,
        embedding_manager: MagicMock,
    ) -> None:
        """Setup full system with data."""
        # Clean DB
        with db_manager._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("TRUNCATE TABLE verses CASCADE;")
                cursor.execute("TRUNCATE TABLE scriptures CASCADE;")

                # Insert data
                cursor.execute(
                    "INSERT INTO scriptures (id, name) VALUES (1, 'Gita') RETURNING id"
                )
                scripture_id = cursor.fetchone()[0]

                text = "Yoga is the journey of the self."
                cursor.execute(
                    "INSERT INTO verses (scripture_id, chapter_number, verse_number, verse_text, translation_en) VALUES (%s, 6, 1, %s, %s) RETURNING id",
                    (scripture_id, text, text),
                )
                verse_id = cursor.fetchone()[0]

                emb = embedding_manager.embed_text(text)
                emb_str = "[" + ",".join(str(e) for e in emb) + "]"
                cursor.execute(
                    "INSERT INTO scripture_embeddings (verse_id, embedding, language) VALUES (%s, %s, 'en')",
                    (verse_id, emb_str),
                )
            conn.commit()

        # Clean Graph
        graph_builder.clear_graph()
        graph_builder.create_entity("Yoga", "Concept", {"description": "Union"})

    def test_query_flow(
        self, db_manager: DatabaseManager, graph_builder: GraphBuilder
    ) -> None:
        """Test the full query flow."""
        # Mock LLM client to avoid external calls
        with (
            patch("src.agent.vidwaan_agent.LMStudioClient") as MockClient,
            patch(
                "src.retrieval.advanced_retrieval_pipeline.ContextAwareReranker"
            ) as MockReranker,
            patch("src.agent.vidwaan_agent.MultilingualSearch") as MockMultiSearch,
        ):
            # Setup Reranker mock
            mock_reranker_instance = MockReranker.return_value
            mock_reranker_instance.rerank.side_effect = lambda q, docs, top_k=5: docs[
                :top_k
            ]

            # Setup MultilingualSearch mock
            mock_search_instance = MockMultiSearch.return_value
            mock_search_instance.process_query.return_value = {
                "language_code": "en",
                "embedding": [0.1] * 1024,
                "processed_text": "What is Yoga?",
            }

            mock_llm = MockClient.return_value
            mock_llm.generate.return_value = "Yoga is a spiritual practice."

            # Initialize Agent
            from src.core.config import settings

            agent = VidwaanAI(
                db_url=settings.DATABASE_URL,
                openai_key="test-key",
                use_lmstudio=True,
                lmstudio_url="http://localhost:1234/v1",
                enable_graph_rag=True,
                neo4j_uri=settings.NEO4J_URI,
                neo4j_user=settings.NEO4J_USER,
                neo4j_password=settings.NEO4J_PASSWORD,
            )
            # Inject mocked embedding manager if possible, or patch it
            # VidwaanAI initializes its own EmbeddingManager. We should patch it.

            with patch("src.agent.vidwaan_agent.EmbeddingManager") as MockEmbed:
                mock_embed_instance = MockEmbed.return_value
                mock_embed_instance.embed_text.return_value = [0.1] * 1024

                response = agent.query("What is Yoga?")

                assert response is not None
                assert "Yoga" in response["answer"]
                # Verify DB log
                # (Optional) check user_queries table

                agent.close()

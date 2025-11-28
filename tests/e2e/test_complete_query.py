import pytest
from src.agent.vidwaan_agent import VidwaanAI
from src.db.db_manager import DatabaseManager
from src.graph.graph_builder import GraphBuilder
from src.rag.embeddings import EmbeddingManager
import os
from unittest.mock import MagicMock, patch

# Mark as e2e test
pytestmark = pytest.mark.e2e

class TestCompleteQuery:
    
    @pytest.fixture(scope="class")
    def db_manager(self):
        return DatabaseManager(os.getenv("DATABASE_URL"))

    @pytest.fixture(scope="class")
    def graph_builder(self):
        uri = os.getenv("NEO4J_URI")
        user = os.getenv("NEO4J_USER")
        password = os.getenv("NEO4J_PASSWORD")
        password = os.getenv("NEO4J_PASSWORD")
        builder = GraphBuilder(uri, user, password)
        yield builder
        builder.close()

    @pytest.fixture(scope="class")
    def embedding_manager(self):
        # Mock embedding manager to return 768 dim vectors
        manager = MagicMock()
        manager.embed_text.side_effect = lambda text: [0.1] * 768
        manager.embed_batch.side_effect = lambda texts: [[0.1] * 768 for _ in texts]
        return manager

    @pytest.fixture(autouse=True)
    def setup_system(self, db_manager, graph_builder, embedding_manager):
        """Setup full system with data."""
        # Clean DB
        with db_manager._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("TRUNCATE TABLE verses CASCADE;")
                cursor.execute("TRUNCATE TABLE scriptures CASCADE;")
                
                # Insert data
                cursor.execute("INSERT INTO scriptures (id, name) VALUES (1, 'Gita') RETURNING id")
                scripture_id = cursor.fetchone()[0]
                
                text = "Yoga is the journey of the self."
                cursor.execute(
                    "INSERT INTO verses (scripture_id, chapter_number, verse_number, verse_text, translation_en) VALUES (%s, 6, 1, %s, %s) RETURNING id",
                    (scripture_id, text, text)
                )
                verse_id = cursor.fetchone()[0]
                
                emb = embedding_manager.embed_text(text)
                emb_str = "[" + ",".join(str(e) for e in emb) + "]"
                cursor.execute(
                    "INSERT INTO scripture_embeddings (verse_id, embedding, language) VALUES (%s, %s, 'en')",
                    (verse_id, emb_str)
                )
            conn.commit()
            
        # Clean Graph
        graph_builder.clear_graph()
        graph_builder.create_concept("Yoga", {"description": "Union"})

    def test_query_flow(self, db_manager, graph_builder):
        """Test the full query flow."""
        # Mock LLM client to avoid external calls
        with patch('src.agent.vidwaan_agent.LMStudioClient') as MockClient:
            mock_llm = MockClient.return_value
            mock_llm.generate.return_value = "Yoga is a spiritual practice."
            
            # Initialize Agent
            agent = VidwaanAI(
                db_url=os.getenv("DATABASE_URL"),
                openai_key="test-key",
                use_lmstudio=True,
                lmstudio_url="http://localhost:1234/v1",
                enable_graph_rag=True,
                neo4j_uri=os.getenv("NEO4J_URI"),
                neo4j_user=os.getenv("NEO4J_USER"),
                neo4j_password=os.getenv("NEO4J_PASSWORD")
            )
            # Inject mocked embedding manager if possible, or patch it
            # VidwaanAI initializes its own EmbeddingManager. We should patch it.
            
            with patch('src.agent.vidwaan_agent.EmbeddingManager') as MockEmbed:
                mock_embed_instance = MockEmbed.return_value
                mock_embed_instance.embed_text.return_value = [0.1] * 768
                
                response = agent.query("What is Yoga?")
                
                assert response is not None
                assert "Yoga" in response["answer"]
                # Verify DB log
                # (Optional) check user_queries table
                
                agent.close()

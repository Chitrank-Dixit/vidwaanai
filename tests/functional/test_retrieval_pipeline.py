import pytest
from src.db.db_manager import DatabaseManager
from src.rag.embeddings import EmbeddingManager
import os

# Mark as functional test
pytestmark = pytest.mark.functional


class TestRetrievalPipeline:
    @pytest.fixture(scope="class")
    def db_manager(self):
        # Use test database URL from settings
        from src.core.config import settings

        db_url = settings.DATABASE_URL
        manager = DatabaseManager(db_url)
        return manager

    @pytest.fixture(scope="class")
    def embedding_manager(self):
        # Mock embedding manager to return 384 dim vectors to match DB schema
        from unittest.mock import MagicMock

        manager = MagicMock()
        manager.embed_text.side_effect = lambda text: [0.1] * 384
        manager.embed_batch.side_effect = lambda texts: [[0.1] * 384 for _ in texts]
        return manager

    @pytest.fixture(autouse=True)
    def setup_data(self, db_manager, embedding_manager):
        """Insert sample data for testing."""
        # Clear existing data
        with db_manager._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("TRUNCATE TABLE verses CASCADE;")
                cursor.execute("TRUNCATE TABLE scriptures CASCADE;")

                # Insert scripture
                cursor.execute(
                    "INSERT INTO scriptures (id, name, description) VALUES (1, 'Test Scripture', 'Description') RETURNING id;"
                )
                scripture_id = cursor.fetchone()[0]

                # Insert verses with embeddings
                texts = [
                    "Dharma protects those who protect it.",
                    "Karma is the law of cause and effect.",
                    "Yoga is skill in action.",
                ]

                embeddings = embedding_manager.embed_batch(texts)

                for i, (text, emb) in enumerate(zip(texts, embeddings)):
                    cursor.execute(
                        """
                        INSERT INTO verses (scripture_id, chapter_number, verse_number, verse_text, translation_en)
                        VALUES (%s, 1, %s, %s, %s) RETURNING id;
                        """,
                        (scripture_id, i + 1, text, text),
                    )
                    verse_id = cursor.fetchone()[0]

                    # Insert embedding
                    # Format embedding as string for pgvector
                    embedding_str = "[" + ",".join(str(e) for e in emb) + "]"
                    cursor.execute(
                        """
                        INSERT INTO scripture_embeddings (verse_id, embedding, language)
                        VALUES (%s, %s, 'en');
                        """,
                        (verse_id, embedding_str),
                    )
            conn.commit()

    def test_vector_search(self, db_manager, embedding_manager):
        """Test retrieving similar verses."""
        query = "What is duty?"
        query_embedding = embedding_manager.embed_text(query)

        results = db_manager.retrieve_verses(query_embedding, top_k=2)

        assert len(results) > 0
        assert "similarity" in results[0]
        # Dharma verse should be relevant to duty
        assert any("Dharma" in r["text"] for r in results)

    def test_keyword_search(self, db_manager):
        """Test simple keyword filtering (if implemented) or just DB retrieval."""
        # This assumes retrieve_verses handles vector search primarily
        # But we can test basic DB fetch
        verses = db_manager.get_all_verses()
        assert len(verses) == 3

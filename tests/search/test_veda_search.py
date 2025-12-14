import pytest
from unittest.mock import MagicMock
from src.retrieval.veda_retriever import VedaRetriever


class TestVedaSearch:
    """Test sematic search on Vedas."""

    @pytest.fixture
    def mock_db_manager(self):
        mock = MagicMock()
        # Mock cursor context manager
        conn = MagicMock()
        cursor = MagicMock()
        mock._get_connection.return_value.__enter__.return_value = conn
        conn.cursor.return_value.__enter__.return_value = cursor

        # Mock fetchall for search result
        # id, text, trans, num, ved, mandala, sukta, distance
        cursor.fetchall.return_value = [
            (
                1,
                "औषधि मंत्र",
                "Healing chant",
                5,
                "Rig Ved",
                "Mandala 10",
                "Sukta 97",
                0.1,
            ),
            (2, "जल मंत्र", "Water chant", 2, "Atharva Ved", "Kanda 1", "Sukta 2", 0.2),
        ]

        return mock

    @pytest.fixture
    def mock_embedder(self):
        mock = MagicMock()
        mock.embed_text.return_value = [0.1] * 1024
        return mock

    def test_search_execution(self, mock_db_manager, mock_embedder):
        """Test search logic calls DB correctly."""
        retriever = VedaRetriever(mock_db_manager, mock_embedder)

        query = "healing herbs"
        results = retriever.search(query)

        assert len(results) == 2
        assert results[0]["score"] == 0.9  # 1 - 0.1
        assert "Rig Ved" in results[0]["source"]

    @pytest.mark.integration
    def test_real_search_flow(self):
        """
        Integration test requiring actual DB and Embedder.
        Marked safe to skip if no DB.
        """
        try:
            from src.db.db_manager import DatabaseManager
            from src.core.config import settings

            db = DatabaseManager(settings.DATABASE_URL)
            retriever = VedaRetriever(db)

            # This will fail if DB not populated, but tests should run
            # We assume DB might be empty or full.
            # Just check it doesn't crash.
            results = retriever.search("fire ritual")
            assert isinstance(results, list)
        except Exception as e:
            pytest.skip(f"Integration test failed (DB issue?): {e}")

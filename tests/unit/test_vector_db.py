import pytest
import unittest
from unittest.mock import MagicMock, patch
from src.db.db_manager import DatabaseManager


class TestVectorDB:
    @pytest.fixture
    def mock_pool(self):
        with patch("src.db.db_manager.ThreadedConnectionPool") as mock_pool_cls:
            yield mock_pool_cls

    @pytest.fixture
    def db_manager(self, mock_pool):
        return DatabaseManager("postgresql://user:pass@localhost:5432/db")

    def test_add_embedding(self, db_manager):
        # Mock connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()

        # Setup pool to return mock connection
        db_manager.pool.getconn.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

        # Execute
        embedding = [0.1, 0.2, 0.3]
        db_manager.add_embedding(verse_id=1, embedding=embedding, language="en")

        # Verify
        mock_cursor.execute.assert_called_once()
        args = mock_cursor.execute.call_args[0]
        sql = args[0]
        params = args[1]

        assert "INSERT INTO scripture_embeddings" in sql
        assert params[0] == 1
        assert params[1] == "[0.1,0.2,0.3]"  # String format for pgvector
        assert params[2] == "en"

        mock_conn.commit.assert_called_once()
        db_manager.pool.putconn.assert_called_with(mock_conn)

    def test_retrieve_verses(self, db_manager):
        # Mock connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()

        db_manager.pool.getconn.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

        # Mock fetchall return
        mock_cursor.fetchall.return_value = [
            {
                "id": 1,
                "scripture": "Gita",
                "chapter": 1,
                "verse": 1,
                "text": "Text",
                "translation": "Trans",
                "similarity": 0.9,
            }
        ]

        # Execute
        query_embedding = [0.1, 0.2, 0.3]
        results = db_manager.retrieve_verses(query_embedding, top_k=5)

        # Verify
        assert len(results) == 1
        assert results[0]["id"] == 1

        mock_cursor.execute.assert_called_once()
        args = mock_cursor.execute.call_args[0]
        sql = args[0]
        params = args[1]

        assert "SELECT DISTINCT" in sql
        assert "similarity" in sql
        assert params[0] == "[0.1,0.2,0.3]"
        assert params[-1] == 5

    def test_retrieve_verses_fallback(self, db_manager):
        # Simulate vector search failure
        mock_conn = MagicMock()
        mock_cursor = MagicMock()

        db_manager.pool.getconn.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

        # First execution raises exception
        mock_cursor.execute.side_effect = [Exception("Vector error"), None]

        # Second execution (fallback) returns results
        mock_cursor.fetchall.side_effect = [
            [
                {
                    "id": 1,
                    "scripture": "Gita",
                    "chapter": 1,
                    "verse": 1,
                    "text": "Text",
                    "translation": "Trans",
                }
            ]  # Fallback result
        ]

        # Execute
        query_embedding = [0.1, 0.2, 0.3]
        results = db_manager.retrieve_verses(query_embedding, top_k=5)

        # Verify
        assert len(results) == 1
        assert results[0]["similarity"] == 0.95  # Fallback similarity

        assert mock_cursor.execute.call_count == 2
        mock_conn.rollback.assert_called_once()

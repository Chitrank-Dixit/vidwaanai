import pytest
import time
from typing import Generator
from unittest.mock import patch, MagicMock
from src.agent.vidwaan_agent import VidwaanAI


class TestPerformance:
    @pytest.fixture
    def mock_deps(
        self,
    ) -> Generator[tuple[MagicMock, MagicMock, MagicMock, MagicMock], None, None]:
        with (
            patch("src.agent.vidwaan_agent.DatabaseManager") as mock_db,
            patch("src.agent.vidwaan_agent.OpenAIClient") as mock_llm,
            patch("src.agent.vidwaan_agent.MultilingualSearch") as mock_multi,
            patch("src.agent.vidwaan_agent.VedaRetriever") as mock_veda,
        ):
            yield mock_db, mock_llm, mock_multi, mock_veda

    @pytest.fixture
    def agent(self, mock_deps: tuple[MagicMock, MagicMock, MagicMock, MagicMock]) -> VidwaanAI:
        mock_db, mock_llm, mock_multi, mock_veda = mock_deps
        mock_db.return_value.get_all_verses.return_value = [
            {"text": "Dummy verse", "id": 1}
        ]
        mock_veda.return_value.search.return_value = []

        # Setup fast mocks
        mock_multi.return_value.process_query.return_value = {
            "language_code": "en",
            "embedding": [0.1] * 384,
            "processed_text": "query",
        }
        mock_db.return_value.retrieve_verses.return_value = [
            {"text": "Verse", "similarity": 0.9, "id": 101}
        ]
        mock_llm.return_value.generate.return_value = "Answer"

        agent = VidwaanAI(
            db_url="postgresql://user:pass@localhost:5432/db",
            openai_key="fake",
            use_lmstudio=False,
        )
        return agent

    def test_query_overhead(self, agent: VidwaanAI) -> None:
        # Measure time taken by agent logic excluding heavy DB/LLM (which are mocked and fast)
        # This tests the overhead of routing, formatting, logging, etc.

        start = time.time()
        agent.query("Test query")
        duration = time.time() - start

        # Should be very fast with mocks (< 0.5s)
        assert duration < 0.5

    def test_concurrent_overhead(self, agent: VidwaanAI) -> None:
        # Simulate sequential requests to check for memory leaks or accumulating latency
        start = time.time()
        for _ in range(100):
            agent.query("Test query")
        duration = time.time() - start

        # 100 queries should be fast
        assert duration < 2.0  # Allow 20ms per query overhead

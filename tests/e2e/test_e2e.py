import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from typing import Generator
from src.api.main import app
from src.api.routes import get_agent_service


class TestE2E:
    @pytest.fixture
    def client(self) -> TestClient:
        return TestClient(app)

    @pytest.fixture
    def mock_agent(self) -> Generator[MagicMock, None, None]:
        mock = MagicMock()
        app.dependency_overrides[get_agent_service] = lambda: mock
        yield mock
        app.dependency_overrides = {}

    def test_user_journey(self, client: TestClient, mock_agent: MagicMock) -> None:
        """
        Simulate a user journey:
        1. User checks health.
        2. User queries in English.
        3. User queries in Hindi.
        """

        # 1. Health Check
        resp = client.get("/api/v1/agent/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "healthy"

        # 2. English Query
        mock_agent.process_query.return_value = {
            "answer": "Answer EN",
            "sources": [],
            "reasoning_trace": [],
            "session_id": "test-session",
            "processing_time_ms": 100.0,
            "language": "en",
            "confidence": 90.0,
            "timestamp": 1704067200.0,
        }

        resp = client.post("/api/v1/agent/query", json={"question": "Query EN"})
        assert resp.status_code == 200
        assert resp.json()["answer"] == "Answer EN"

        # 3. Hindi Query
        mock_agent.process_query.return_value = {
            "answer": "Answer HI",
            "sources": [],
            "reasoning_trace": [],
            "session_id": "test-session",
            "processing_time_ms": 100.0,
            "language": "hi",
            "confidence": 90.0,
            "timestamp": 1704067200.0,
        }

        resp = client.post("/api/v1/agent/query", json={"question": "Query HI", "language": "hi"})
        assert resp.status_code == 200
        assert resp.json()["answer"] == "Answer HI"

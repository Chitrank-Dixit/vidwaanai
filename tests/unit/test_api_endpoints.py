import pytest
from typing import Generator
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
from src.api.main import app
from src.api.routes import get_agent_service


class TestAPIEndpoints:
    @pytest.fixture
    def client(self) -> TestClient:
        return TestClient(app)

    @pytest.fixture
    def mock_agent(self) -> Generator[MagicMock, None, None]:
        # Override the get_agent dependency
        mock_agent_instance = MagicMock()
        app.dependency_overrides[get_agent_service] = lambda: mock_agent_instance
        yield mock_agent_instance
        app.dependency_overrides = {}

    def test_health_check(self, client: TestClient) -> None:
        response = client.get("/api/v1/agent/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"

    def test_query_endpoint(self, client: TestClient, mock_agent: MagicMock) -> None:
        # Mock agent response
        mock_agent.process_query.return_value = {
            "answer": "Test answer",
            "confidence": 100.0,
            "sources": [],
            "reasoning_trace": [],
            "session_id": "test-session",
            "processing_time_ms": 100.0,
            "timestamp": 1704067200.0,  # 2024-01-01 timestamp
        }

        payload = {"question": "What is life?", "language": "en"}

        response = client.post("/api/v1/agent/query", json=payload)

        assert response.status_code == 200
        data = response.json()
        assert data["answer"] == "Test answer"

        mock_agent.process_query.assert_called_once()
        args = mock_agent.process_query.call_args[1]
        assert args["question"] == "What is life?"

    def test_query_endpoint_missing_field(
        self, client: TestClient, mock_agent: MagicMock
    ) -> None:
        payload = {
            "language": "en"
            # Missing question
        }
        response = client.post("/api/v1/agent/query", json=payload)
        assert response.status_code == 422  # Validation error

    def test_query_endpoint_error(
        self, client: TestClient, mock_agent: MagicMock
    ) -> None:
        mock_agent.process_query.side_effect = Exception("Internal error")

        payload = {"question": "Error query"}

        response = client.post("/api/v1/agent/query", json=payload)
        assert response.status_code == 500
        assert "Internal error" in response.json()["detail"]

    def test_get_agent_dependency(self) -> None:
        """Test the get_agent dependency function directly"""
        with patch("src.api.routes.AgentService") as MockAgentService:
            # Clear app.state.agent if it exists
            # Note: get_agent_service uses lru_cache, not app.state

            # We need to clear lru_cache for the test to verify instantiation
            get_agent_service.cache_clear()

            # First call should initialize agent
            agent1 = get_agent_service()
            assert agent1 is not None
            MockAgentService.assert_called_once()

            # Second call should return cached agent
            agent2 = get_agent_service()
            assert agent2 is agent1
            MockAgentService.assert_called_once()  # Should still be called only once

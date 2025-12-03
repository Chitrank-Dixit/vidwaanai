import pytest
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
from src.api import app, get_agent


class TestAPIEndpoints:
    @pytest.fixture
    def client(self):
        return TestClient(app)

    @pytest.fixture
    def mock_agent(self):
        # Override the get_agent dependency
        mock_agent_instance = MagicMock()
        app.dependency_overrides[get_agent] = lambda: mock_agent_instance
        yield mock_agent_instance
        app.dependency_overrides = {}

    def test_health_check(self, client):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}

    def test_query_endpoint(self, client, mock_agent):
        # Mock agent response
        mock_agent.query.return_value = {
            "answer": "Test answer",
            "retrieved_verses": [],
            "language": "en",
            "confidence": {"score": 100, "warning": None},
            "timestamp": "2024-01-01T00:00:00",
        }

        payload = {"text": "What is life?", "language": "en"}

        response = client.post("/query", json=payload)

        assert response.status_code == 200
        data = response.json()
        assert data["answer"] == "Test answer"
        assert data["language"] == "en"

        mock_agent.query.assert_called_once()
        args = mock_agent.query.call_args[1]
        assert args["question"] == "What is life?"
        assert args["language"] == "en"

    def test_query_endpoint_missing_field(self, client, mock_agent):
        payload = {
            "language": "en"
            # Missing text
        }
        response = client.post("/query", json=payload)
        assert response.status_code == 422  # Validation error

    def test_query_endpoint_error(self, client, mock_agent):
        mock_agent.query.side_effect = Exception("Internal error")

        payload = {"text": "Error query"}

        response = client.post("/query", json=payload)
        assert response.status_code == 500
        assert "Internal error" in response.json()["detail"]

    def test_get_agent_dependency(self):
        """Test the get_agent dependency function directly"""
        with patch("src.api.VidwaanAI") as MockVidwaanAI:
            # Clear app.state.agent if it exists
            if hasattr(app.state, "agent"):
                del app.state.agent

            # First call should initialize agent
            agent1 = get_agent()
            assert agent1 is not None
            MockVidwaanAI.assert_called_once()

            # Second call should return cached agent
            agent2 = get_agent()
            assert agent2 is agent1
            MockVidwaanAI.assert_called_once()  # Should still be called only once

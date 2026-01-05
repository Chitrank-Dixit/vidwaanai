import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock

from src.api.main import app
from src.api.routes import get_agent_service
from src.core.agent_service import AgentService

client = TestClient(app)


@pytest.fixture
def mock_agent_service():
    """Mock the AgentService dependency using FastAPI overrides"""
    service_mock = Mock(spec=AgentService)
    # Mock process_query return value
    service_mock.process_query.return_value = {
        "answer": "Test Answer",
        "confidence": 0.99,
        "sources": [],
        "reasoning_trace": [],
        "session_id": "test-session",
        "timestamp": 1234567890.0,
        "processing_time_ms": 100.0,
    }

    # Override dependency
    app.dependency_overrides[get_agent_service] = lambda: service_mock
    yield service_mock
    # Cleanup
    app.dependency_overrides = {}


def test_health_check(mock_agent_service):
    """Test GET /health"""
    response = client.get("/api/v1/agent/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_query_agent_success(mock_agent_service):
    """Test POST /query with valid input"""
    payload = {"question": "What is unit testing?", "session_id": "session-123"}
    response = client.post("/api/v1/agent/query", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["answer"] == "Test Answer"

    # Verify service was called correctly
    mock_agent_service.process_query.assert_called_once()


def test_query_agent_error(mock_agent_service):
    """Test POST /query handling service errors"""
    # Simulate service failure
    mock_agent_service.process_query.side_effect = Exception("Service Failure")

    payload = {"question": "Crash me"}
    response = client.post("/api/v1/agent/query", json=payload)

    assert response.status_code == 500
    # Error detail might be wrapped in JSON
    # 'detail': 'Error processing query: Service Failure'
    assert "Service Failure" in response.json()["detail"]


def test_create_session():
    """Test POST /session/create"""
    response = client.post("/api/v1/agent/session/create", json={"title": "My Chat"})
    assert response.status_code == 200
    data = response.json()
    assert "session_id" in data
    assert data["title"] == "My Chat"

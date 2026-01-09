from unittest.mock import MagicMock
from fastapi.testclient import TestClient
from src.api.main import app
from src.api.dependencies import get_agent_service

client = TestClient(app)

# Mock AgentService
mock_service = MagicMock()
mock_retriever = MagicMock()
mock_service.retriever = mock_retriever


def override_get_agent_service():
    return mock_service


app.dependency_overrides[get_agent_service] = override_get_agent_service


def test_hybrid_search_endpoint():
    # Setup mock return
    mock_retriever.search.return_value = [
        {
            "id": "1",
            "text": "Mantra Text",
            "translation": "Translation",
            "source": "RV 1.1.1",
            "score": 0.95,
            "fusion_method": "rrf",
        }
    ]

    response = client.get("/api/v1/search/hybrid?q=agni&limit=5&fusion=rrf")

    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 1
    assert data["results"][0]["id"] == "1"
    assert data["results"][0]["retrieval_method"] == "rrf"

    mock_retriever.search.assert_called_with(
        query="agni", top_k=5, strategy="hybrid", fusion_method="rrf"
    )


def test_hybrid_search_invalid_params():
    response = client.get("/api/v1/search/hybrid?q=agni&fusion=invalid")
    assert response.status_code == 422  # Validation error

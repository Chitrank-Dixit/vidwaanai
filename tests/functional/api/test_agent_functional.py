import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

from src.api.main import app

# Create client
client = TestClient(app)


@pytest.fixture
def mock_external_deps():
    """
    Mock external dependencies of AgentService:
    - DatabaseManager
    - VedaEmbedder
    - LMStudioClient
    - GraphBuilder
    """
    with (
        patch("src.core.agent_service.DatabaseManager") as MockDB,
        patch("src.core.agent_service.VedaEmbedder") as MockEmbedder,
        patch("src.core.agent_service.LMStudioClient") as MockLLM,
        patch("src.core.agent_service.GraphBuilder") as MockGraph,
    ):

        # Setup mocks
        db_instance = MockDB.return_value
        # Mock connection context manager
        conn_mock = MagicMock()
        cursor_mock = MagicMock()
        db_instance._get_connection.return_value.__enter__.return_value = conn_mock
        conn_mock.cursor.return_value.__enter__.return_value = cursor_mock

        # Mock vector search results
        # row: id, text, translation, mantra_num, ved_name, chapter, hymn, distance
        cursor_mock.fetchall.return_value = [
            (1, "Agni is fire", "Translation...", 1, "Rig Ved", "1", "1", 0.1),
            (2, "Vayu is wind", "Translation...", 2, "Yajur Ved", "1", "2", 0.2),
        ]

        embedder_instance = MockEmbedder.return_value
        embedder_instance.embed_text.return_value = [0.1] * 1024

        llm_instance = MockLLM.return_value
        # First call is NER (expects JSON), second is Answer (text)
        llm_instance.generate.side_effect = [
            '[{"name": "Agni", "type": "Deity"}]', 
            "This is a functional test answer."
        ]

        yield {
            "db": db_instance,
            "embedder": embedder_instance,
            "llm": llm_instance,
            "graph": MockGraph.return_value,
        }


def test_query_flow_functional(mock_external_deps):
    """
    Functional test:
    - Instantiates REAL AgentService (via dependency override or natural flow?)
    - Mocks only the DB/LLM layers.
    - Verifies proper wiring (AgentService calls Embedder -> DB -> LLM).
    """

    # We need to ensure the App uses a fresh AgentService that picks up our mocks
    # Since we patched the class constructors 'src.core.agent_service.DatabaseManager',
    # any new AgentService() will use these mocks.
    # However, 'get_agent_service' is lru_cached in routes.py!
    # We must clear that cache or override dependency.

    from src.api.routes import get_agent_service

    get_agent_service.cache_clear()

    payload = {"question": "Functional Check", "session_id": "func-1"}
    response = client.post("/api/v1/agent/query", json=payload)

    assert response.status_code == 200
    data = response.json()

    # Verify content from our LLM mock
    assert data["answer"] == "This is a functional test answer."
    assert len(data["sources"]) == 2
    # Validating title format from retrieval: "{ved} {chapter} {hymn}"
    # Mock row[4]="Rig Ved", row[5]="1", row[6]="1" -> "Rig Ved 1 1"
    # But wait, VedaRetriever sets 'source', does it set 'title'?
    # AgentService sets title as "Unknown Source" if not present, or 'source' key?
    # Let's check AgentService response construction.
    # It uses d['source'] or d['title'].
    # VedaRetriever returns 'source'.
    assert "Rig Ved" in data["sources"][0]["title"]

    # Verify Orchestration
    # Embedder called?
    assert mock_external_deps["embedder"].embed_text.call_count >= 1
    # DB called?
    # cursor mock should have executed params
    # LLM called?
    # LLM called? (NER + Answer = 2 calls usually)
    assert mock_external_deps["llm"].generate.call_count >= 1


def test_validation_error_functional():
    """Test standard Pydantic validation (422)"""
    # Missing 'question'
    response = client.post("/api/v1/agent/query", json={"session_id": "bad"})
    assert response.status_code == 422


def test_service_error_handling(mock_external_deps):
    """Test 500 handling when internal component fails"""
    # Make LLM fail
    mock_external_deps["llm"].generate.side_effect = Exception("LLM Timeout")

    from src.api.routes import get_agent_service

    get_agent_service.cache_clear()

    response = client.post("/api/v1/agent/query", json={"question": "fail"})
    assert response.status_code == 500
    assert "LLM Timeout" in response.json()["detail"]

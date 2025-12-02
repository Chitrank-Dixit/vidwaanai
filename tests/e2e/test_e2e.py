import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from src.api import app, get_agent

class TestE2E:
    
    @pytest.fixture
    def client(self):
        return TestClient(app)

    @pytest.fixture
    def mock_agent(self):
        mock = MagicMock()
        app.dependency_overrides[get_agent] = lambda: mock
        yield mock
        app.dependency_overrides = {}

    def test_user_journey(self, client, mock_agent):
        """
        Simulate a user journey:
        1. User checks health.
        2. User queries in English.
        3. User queries in Hindi.
        """
        
        # 1. Health Check
        resp = client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "healthy"
        
        # 2. English Query
        mock_agent.query.return_value = {
            "answer": "Answer EN",
            "retrieved_verses": [],
            "language": "en",
            "confidence": {"score": 90, "level": "High"},
            "timestamp": "2024-01-01"
        }
        
        resp = client.post("/query", json={"text": "Query EN"})
        assert resp.status_code == 200
        assert resp.json()["answer"] == "Answer EN"
        assert resp.json()["language"] == "en"
        
        # 3. Hindi Query
        mock_agent.query.return_value = {
            "answer": "Answer HI",
            "retrieved_verses": [],
            "language": "hi",
            "confidence": {"score": 90, "level": "High"},
            "timestamp": "2024-01-01"
        }
        
        resp = client.post("/query", json={"text": "Query HI", "language": "hi"})
        assert resp.status_code == 200
        assert resp.json()["answer"] == "Answer HI"
        assert resp.json()["language"] == "hi"

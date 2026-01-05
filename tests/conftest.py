import pytest
import os
import sys
from typing import Dict, Any
from unittest.mock import MagicMock
from fastapi.testclient import TestClient

# Add src to python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.config import Settings
from src.db.db_manager import DatabaseManager
from src.retrieval.veda_retriever import VedaRetriever
from src.api.main import app


@pytest.fixture
def mock_settings() -> Settings:
    return Settings(
        DATABASE_URL="postgresql://user:pass@localhost:5432/test_db",
        NEO4J_URI="bolt://localhost:7687",
        NEO4J_USER="neo4j",
        NEO4J_PASSWORD="password",
        OPENAI_API_KEY="test-key",
        lmstudio_base_url="http://localhost:1234/v1",
        llm_backend="mock",
    )


@pytest.fixture
def mock_llm_client() -> MagicMock:
    client = MagicMock()
    client.generate.return_value = "Mocked LLM response"
    client.get_embedding.return_value = [0.1] * 768
    return client


@pytest.fixture
def mock_db_manager() -> MagicMock:
    db = MagicMock(spec=DatabaseManager)
    db.get_all_verses.return_value = []
    db.retrieve_verses.return_value = []
    db.get_scriptures.return_value = [{"id": 1, "name": "Rig Veda"}]
    return db


@pytest.fixture
def mock_veda_retriever(mock_db_manager: MagicMock) -> MagicMock:
    retriever = MagicMock(spec=VedaRetriever)
    retriever.search.return_value = [
        {
            "source": "Rig Veda Mandala 1 Sukta 1",
            "mantra_num": 1,
            "text": "Agnim ile purohitam",
            "translation": "I praise Agni, the priest",
            "score": 0.95,
        }
    ]
    return retriever


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


# Note: AsyncClient requires httpx installed.
# Using TestClient (sync) for now which covers most FastAPI testing needs unless specific async flow is blocked.
# If AsyncClient needed:
# from httpx import AsyncClient
# @pytest.fixture
# async def async_client() -> AsyncGenerator:
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         yield ac


@pytest.fixture
def sample_verse() -> Dict[str, Any]:
    return {
        "id": 1,
        "scripture_id": 1,
        "chapter_number": 2,
        "verse_number": 47,
        "verse_text": "Karmanye vadhikaraste ma phaleshu kadachana",
        "translation_en": "You have a right to perform your prescribed duty, but you are not entitled to the fruits of action.",
        "scripture_name": "Bhagavad Gita",
    }


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default=None,
        help="Language code to test (e.g., hi, en)",
    )
    parser.addoption(
        "--category",
        action="store",
        default=None,
        help="Category to test (e.g., ramayana)",
    )


@pytest.fixture
def language(request):
    return request.config.getoption("--language")


@pytest.fixture
def category(request):
    return request.config.getoption("--category")

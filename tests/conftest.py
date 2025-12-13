import pytest
import os
import sys
from typing import Dict, Any
from unittest.mock import MagicMock

# Add src to python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.config import Settings


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

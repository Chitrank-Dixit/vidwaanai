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


@pytest.fixture(scope="session", autouse=True)
def init_test_db():
    """Initialize test database schema (both generic and vedic) for all tests."""
    from src.db.db_manager import DatabaseManager
    # Use generic database URL for testing if not set
    db_url = os.getenv("DATABASE_URL", "postgresql://vidwaan_user:vidwaan_password@localhost:5432/vidwaan_test")
    
    # Skip if using mock DB in unit tests (checked by connection attempt or env)
    try:
        db = DatabaseManager(db_url)
        with db._get_connection() as conn:
            with conn.cursor() as cursor:
                # Drop all tables to ensure clean state
                cursor.execute(
                    """
                    DROP TABLE IF EXISTS 
                        veda_embeddings, mantras, suktas, mandalas, vedas,
                        scripture_embeddings, verses, scriptures, user_queries, embeddings
                    CASCADE;
                    """
                )

                # 1. Create Generic Schema (from database/init.sql)
                cursor.execute(
                    """
                    CREATE EXTENSION IF NOT EXISTS vector;

                    CREATE TABLE IF NOT EXISTS scriptures (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL UNIQUE,
                        language VARCHAR(50),
                        description TEXT,
                        version VARCHAR(50),
                        loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );

                    CREATE TABLE IF NOT EXISTS verses (
                        id SERIAL PRIMARY KEY,
                        scripture_id INT REFERENCES scriptures(id) ON DELETE CASCADE,
                        chapter_number INT,
                        verse_number INT,
                        verse_text TEXT,
                        translation_en TEXT,
                        themes TEXT[],
                        speakers TEXT[],
                        UNIQUE(scripture_id, chapter_number, verse_number)
                    );

                    CREATE TABLE IF NOT EXISTS scripture_embeddings (
                        id SERIAL PRIMARY KEY,
                        verse_id INT REFERENCES verses(id) ON DELETE CASCADE,
                        embedding vector(1024),
                        language VARCHAR(50),
                        chunk_index INT,
                        processed BOOLEAN,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        UNIQUE(verse_id, language, chunk_index)
                    );

                    CREATE TABLE IF NOT EXISTS user_queries (
                        id SERIAL PRIMARY KEY,
                        query_text TEXT,
                        language VARCHAR(50),
                        response_text TEXT,
                        retrieved_verse_ids INT[],
                        confidence_score FLOAT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                    
                    CREATE TABLE IF NOT EXISTS embeddings (
                        id SERIAL PRIMARY KEY,
                        verse_id INTEGER NOT NULL,
                        embedding TEXT NOT NULL,
                        language VARCHAR(10) NOT NULL,
                        processed BOOLEAN DEFAULT FALSE,
                        UNIQUE (verse_id, language)
                    );
                    """
                )

                # 2. Create Vedic Schema (from scripts/setup_veda_schema.py)
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS vedas (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255),
                        code VARCHAR(255),
                        language VARCHAR(10),
                        total_mantras INT,
                        description TEXT,
                        source_pdf_path TEXT,
                        created_at TIMESTAMP DEFAULT NOW()
                    );
                    
                    CREATE TABLE IF NOT EXISTS mandalas (
                        id SERIAL PRIMARY KEY,
                        ved_id INT NOT NULL REFERENCES vedas(id),
                        mandala_number INT,
                        name VARCHAR(100),
                        description TEXT
                    );
                    
                    CREATE TABLE IF NOT EXISTS suktas (
                        id SERIAL PRIMARY KEY,
                        mandala_id INT NOT NULL REFERENCES mandalas(id),
                        ved_id INT NOT NULL REFERENCES vedas(id),
                        sukta_number INT,
                        name VARCHAR(100),
                        description TEXT
                    );
                    
                    CREATE TABLE IF NOT EXISTS mantras (
                        id SERIAL PRIMARY KEY,
                        ved_id INT NOT NULL REFERENCES vedas(id),
                        sukta_id INT REFERENCES suktas(id),
                        mandala_id INT REFERENCES mandalas(id),
                        mantra_number INT,
                        text_hindi TEXT,
                        text_sanskrit TEXT,
                        translation_en TEXT,
                        meaning_hindi TEXT,
                        tags JSONB,
                        metadata JSONB
                    );
                    
                    CREATE TABLE IF NOT EXISTS veda_embeddings (
                        id SERIAL PRIMARY KEY,
                        mantra_id INT NOT NULL REFERENCES mantras(id),
                        ved_id INT NOT NULL REFERENCES vedas(id),
                        embedding vector(1024),
                        language VARCHAR(10),
                        chunk_type VARCHAR(20),
                        created_at TIMESTAMP DEFAULT NOW()
                    );
                    """
                )

                conn.commit()
    except Exception as e:
        print(f"Skipping DB init (likely unit test env): {e}")



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

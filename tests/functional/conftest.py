import pytest
from src.db.db_manager import DatabaseManager
from src.core.config import settings

@pytest.fixture(scope="session", autouse=True)
def init_test_db():
    """Initialize test database schema (both generic and vedic)."""
    db = DatabaseManager(settings.DATABASE_URL)
    with db._get_connection() as conn:
        with conn.cursor() as cursor:
            # Drop all tables to ensure clean state
            cursor.execute("""
                DROP TABLE IF EXISTS 
                    veda_embeddings, mantras, suktas, mandalas, vedas,
                    scripture_embeddings, verses, scriptures, user_queries, embeddings
                CASCADE;
            """)
            
            # 1. Create Generic Schema (from database/init.sql)
            cursor.execute("""
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
            """)

            # 2. Create Vedic Schema (from scripts/setup_veda_schema.py)
            cursor.execute("""
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
            """)
            
            conn.commit()

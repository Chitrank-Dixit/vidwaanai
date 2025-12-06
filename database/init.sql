-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Scriptures table
CREATE TABLE IF NOT EXISTS scriptures (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    language VARCHAR(50),
    description TEXT,
    version VARCHAR(50),
    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Verses table
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

-- Embeddings table
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

-- Create HNSW index for fast similarity search
CREATE INDEX IF NOT EXISTS idx_embeddings_hnsw ON scripture_embeddings 
USING hnsw (embedding vector_cosine_ops);

-- User queries table (for logging and analytics)
CREATE TABLE IF NOT EXISTS user_queries (
    id SERIAL PRIMARY KEY,
    query_text TEXT,
    language VARCHAR(50),
    response_text TEXT,
    retrieved_verse_ids INT[],
    confidence_score FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create index on created_at
CREATE INDEX IF NOT EXISTS idx_queries_created_at ON user_queries(created_at DESC);

CREATE TABLE IF NOT EXISTS embeddings (
    id SERIAL PRIMARY KEY,
    verse_id INTEGER NOT NULL,
    embedding TEXT NOT NULL,
    language VARCHAR(10) NOT NULL,
    processed BOOLEAN DEFAULT FALSE,
    UNIQUE (verse_id, language)
);



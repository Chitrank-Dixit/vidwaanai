-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Scriptures table
CREATE TABLE IF NOT EXISTS scriptures (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    language VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Verses table
CREATE TABLE IF NOT EXISTS verses (
    id SERIAL PRIMARY KEY,
    scripture_id INTEGER REFERENCES scriptures(id) ON DELETE CASCADE,
    chapter_number INTEGER NOT NULL,
    verse_number INTEGER NOT NULL,
    verse_text TEXT NOT NULL,
    translation_en TEXT,
    themes TEXT[],
    speakers TEXT[],
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(scripture_id, chapter_number, verse_number)
);

-- Scripture Embeddings table
CREATE TABLE IF NOT EXISTS scripture_embeddings (
    id SERIAL PRIMARY KEY,
    verse_id INTEGER REFERENCES verses(id) ON DELETE CASCADE,
    embedding VECTOR(384),
    language VARCHAR(10) NOT NULL,
    chunk_index INTEGER DEFAULT 0,
    processed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(verse_id, language, chunk_index)
);

-- User Queries table
CREATE TABLE IF NOT EXISTS user_queries (
    id SERIAL PRIMARY KEY,
    query_text TEXT NOT NULL,
    language VARCHAR(10),
    response_text TEXT,
    retrieved_verse_ids INTEGER[],
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_verses_scripture_chapter ON verses(scripture_id, chapter_number);
CREATE INDEX IF NOT EXISTS idx_embeddings_verse_id ON scripture_embeddings(verse_id);

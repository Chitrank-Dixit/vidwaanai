-- Create HNSW index for fast similarity search
CREATE INDEX IF NOT EXISTS idx_embeddings_hnsw ON scripture_embeddings 
USING hnsw (embedding vector_cosine_ops);

-- Create index on language for filtering
CREATE INDEX IF NOT EXISTS idx_embeddings_language ON scripture_embeddings(language);

-- Create index on chunk_index for uniqueness checks and ordering
CREATE INDEX IF NOT EXISTS idx_embeddings_chunk ON scripture_embeddings(chunk_index);

-- Create composite index for common query pattern
CREATE INDEX IF NOT EXISTS idx_embeddings_lang_verse ON scripture_embeddings(language, verse_id);

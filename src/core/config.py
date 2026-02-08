from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # tell pydantic-settings to read .env and ignore any keys you haven't modeled yet
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # or 'forbid' if you model all fields below
    )

    # API keys
    OPENAI_API_KEY: Optional[str] = None
    KRUTRIM_API_KEY: Optional[str] = None

    # Database
    DATABASE_URL: str = (
        "postgresql://vidwaan_user:vidwaan_password@localhost:5432/vidwaan_db"
    )

    # LLM / embeddings
    EMBEDDING_MODEL: str = "krutrim-ai-labs/Vyakyarth"
    LLM_MODEL: str = "gpt-4-turbo"

    # NEW: Vyakyarth location hint (optional)
    vyakyarth_model_path: Optional[str] = None  # e.g. "local"

    # NEW: LLM backend selector
    #   "openai"   -> use OpenAIClient
    #   "lmstudio" -> use LMStudioClient
    llm_backend: str = "lmstudio"

    # NEW: LM Studio settings
    lmstudio_base_url: str = "http://localhost:1234"
    lmstudio_model: str = "falcon-h1-7b-instruct"  # or whatever /v1/models shows
    
    # Timeout settings
    LLM_TIMEOUT: int = 300  # Default to 5 minutes

    # RAG settings
    RETRIEVAL_TOP_K: int = 5
    CHUNK_SIZE: int = 1024
    CHUNK_OVERLAP: int = 204

    # Logging
    LOG_LEVEL: str = "INFO"

    # Graph Database
    NEO4J_URI: str = "bolt://localhost:7687"
    NEO4J_USER: str = "neo4j"
    NEO4J_PASSWORD: str = "vidwaan123"

    # Graph RAG settings
    ENABLE_GRAPH_RAG: bool = False
    GRAPH_TRAVERSAL_DEPTH: int = 2
    HYBRID_ALPHA: float = 0.5
    
    # Optimization & Resource Limits
    # Limit graph build concurrency to avoid thrashing LM Studio (CPU bound)
    GRAPH_BUILD_WORKERS: int = 2 
    # Batch size for local embeddings (SentenceTransformer)
    EMBEDDING_BATCH_SIZE: int = 16
    # Global LlamaIndex worker limit (if used)
    LLAMA_INDEX_NUM_WORKERS: int = 2


settings = Settings()

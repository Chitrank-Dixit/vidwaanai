from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

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
    DATABASE_URL: str = "postgresql://vidwaan_user:vidwaan_password@localhost:5432/vidwaan_db"

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

    # RAG settings
    RETRIEVAL_TOP_K: int = 5
    CHUNK_SIZE: int = 1024
    CHUNK_OVERLAP: int = 204

    # Logging
    LOG_LEVEL: str = "INFO"


settings = Settings()

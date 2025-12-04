import time
from typing import Any, Dict, List, Optional

from src.core.logger import get_logger

logger = get_logger(__name__)


class LanguageEmbeddingCache:
    """Cache embeddings for multilingual queries"""

    def __init__(self, max_size: int = 10000, ttl: int = 86400) -> None:
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.max_size = max_size
        self.ttl = ttl

    def _make_key(self, text: str, language: str) -> str:
        return f"{language}:{text}"

    def get_embedding(self, text: str, language: str) -> Optional[List[float]]:
        """Get cached embedding"""
        key = self._make_key(text, language)

        if key in self.cache:
            entry = self.cache[key]
            if time.time() - entry["timestamp"] < self.ttl:
                return list(entry["embedding"])
            else:
                del self.cache[key]
        return None

    def set_embedding(self, text: str, language: str, embedding: List[float]) -> None:
        """Cache embedding"""
        if len(self.cache) >= self.max_size:
            # Simple eviction: remove oldest
            # In a real system, use LRU
            oldest_key = min(
                self.cache.keys(), key=lambda k: self.cache[k]["timestamp"]
            )
            del self.cache[oldest_key]

        key = self._make_key(text, language)
        self.cache[key] = {"embedding": embedding, "timestamp": time.time()}

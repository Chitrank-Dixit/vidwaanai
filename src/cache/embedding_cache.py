from typing import Optional, List, Dict, Any
import time
import hashlib
from src.core.logger import get_logger

logger = get_logger(__name__)


class EmbeddingCache:
    """Cache for generated embeddings."""

    def __init__(self, max_size=10000, ttl=86400):
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.max_size = max_size
        self.ttl = ttl

    def _make_key(self, text: str) -> str:
        """Create a stable key for the text."""
        return hashlib.md5(text.encode("utf-8")).hexdigest()

    def get(self, text: str) -> Optional[List[float]]:
        """Get cached embedding."""
        key = self._make_key(text)

        if key in self.cache:
            entry = self.cache[key]
            if time.time() - entry["timestamp"] < self.ttl:
                return entry["embedding"]
            else:
                del self.cache[key]
        return None

    def set(self, text: str, embedding: List[float]):
        """Cache embedding."""
        if len(self.cache) >= self.max_size:
            # Simple eviction: remove oldest
            oldest_key = min(
                self.cache.keys(), key=lambda k: self.cache[k]["timestamp"]
            )
            del self.cache[oldest_key]

        key = self._make_key(text)
        self.cache[key] = {"embedding": embedding, "timestamp": time.time()}

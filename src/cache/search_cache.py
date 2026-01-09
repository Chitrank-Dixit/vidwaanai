import hashlib
import json
import time
from typing import Any, Dict, List, Optional, cast
import os

from src.cache.redis_cache import RedisCache
from src.core.logger import get_logger


logger = get_logger(__name__)


class SearchCache:
    """Cache for retrieval results (before LLM generation)."""

    def __init__(
        self, max_size: int = 1000, ttl: int = 3600, redis_url: Optional[str] = None
    ) -> None:
        # If REDIS_URL env var is present or passed, use Redis
        self.redis_url = redis_url or os.getenv("REDIS_URL")
        self.redis = RedisCache(self.redis_url, ttl) if self.redis_url else None

        # Fallback in-memory cache
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.max_size = max_size
        self.ttl = ttl

    def _make_key(self, query: str, filters: Optional[Dict[str, Any]] = None) -> str:
        """Create a stable key for query and filters."""
        key_content = {"q": query, "f": filters or {}}
        key_str = json.dumps(key_content, sort_keys=True)
        return "search:" + hashlib.sha256(key_str.encode("utf-8")).hexdigest()

    def get(
        self, query: str, filters: Optional[Dict[str, Any]] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """Get cached search results."""
        key = self._make_key(query, filters)

        # Try Redis first
        if self.redis:
            val = self.redis.get(key)
            if val:
                logger.info(f"Redis cache hit for {key}")
                return cast(List[Dict[str, Any]], val)

        # Fallback to in-memory
        if key in self.cache:
            entry = self.cache[key]
            if time.time() - entry["timestamp"] < self.ttl:
                return list(entry["results"])
            else:
                del self.cache[key]
        return None

    def set(
        self,
        query: str,
        results: List[Dict[str, Any]],
        filters: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Cache search results."""
        key = self._make_key(query, filters)

        # Set in Redis
        if self.redis:
            self.redis.set(key, results)

        # Set in-memory
        if len(self.cache) >= self.max_size:
            # Simple eviction: remove oldest
            oldest_key = min(
                self.cache.keys(), key=lambda k: self.cache[k]["timestamp"]
            )
            del self.cache[oldest_key]

        self.cache[key] = {"results": results, "timestamp": time.time()}

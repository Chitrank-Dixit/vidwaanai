
import logging
import json
import redis
from typing import Any, Optional, Dict
import os

logger = logging.getLogger(__name__)

class RedisCache:
    """Redis-backed cache implementation."""

    def __init__(self, redis_url: str = "redis://localhost:6379", ttl: int = 3600):
        try:
            self.client = redis.from_url(redis_url, decode_responses=True)
            self.ttl = ttl
            logger.info(f"Connected to Redis at {redis_url}")
        except Exception as e:
            logger.error(f"Failed to connect to Redis: {e}")
            self.client = None

    def get(self, key: str) -> Optional[Any]:
        """Get value from cache."""
        if not self.client:
            return None
        try:
            val = self.client.get(key)
            return json.loads(val) if val else None
        except Exception as e:
            logger.error(f"Redis get error: {e}")
            return None

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        """Set value in cache."""
        if not self.client:
            return False
        try:
            return self.client.setex(
                key, 
                ttl or self.ttl, 
                json.dumps(value)
            )
        except Exception as e:
            logger.error(f"Redis set error: {e}")
            return False

import hashlib
import json
import logging
from collections import OrderedDict
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class QueryCache:
    """Simple in-memory LRU cache for query results."""

    def __init__(self, capacity: int = 100):
        self.capacity = capacity
        self.cache: OrderedDict = OrderedDict()
        logger.info(f"Query cache initialized with capacity {capacity}")

    def _generate_key(
        self, question: str, language: str, scripture_filter: Optional[str] = None
    ) -> str:
        """Generate a unique cache key."""
        key_data = {"q": question.strip().lower(), "l": language, "s": scripture_filter}
        key_str = json.dumps(key_data, sort_keys=True)
        return hashlib.md5(key_str.encode()).hexdigest()

    def get(
        self, question: str, language: str, scripture_filter: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """Retrieve a result from the cache."""
        key = self._generate_key(question, language, scripture_filter)
        if key in self.cache:
            # Move to end (most recently used)
            self.cache.move_to_end(key)
            logger.info("Cache hit")
            return self.cache[key]
        return None

    def set(
        self,
        question: str,
        language: str,
        result: Dict[str, Any],
        scripture_filter: Optional[str] = None,
    ) -> None:
        """Store a result in the cache."""
        key = self._generate_key(question, language, scripture_filter)
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = result

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove first (least recently used)

    def clear(self) -> None:
        """Clear the cache."""
        self.cache.clear()

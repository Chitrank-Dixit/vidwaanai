
import pytest
from unittest.mock import MagicMock, patch
import os
from src.cache.search_cache import SearchCache

@pytest.fixture
def mock_redis():
    with patch("src.cache.search_cache.RedisCache") as mock:
        yield mock

def test_search_cache_redis_hit(mock_redis):
    # Setup mock
    mock_instance = mock_redis.return_value
    mock_instance.get.return_value = [{"id": "doc1"}]
    
    # Initialize cache with redis url
    cache = SearchCache(redis_url="redis://test")
    
    # Test get
    result = cache.get("query")
    assert result == [{"id": "doc1"}]
    mock_instance.get.assert_called_once()

def test_search_cache_fallback(mock_redis):
    # Setup mock to return None (miss)
    mock_instance = mock_redis.return_value
    mock_instance.get.return_value = None
    
    cache = SearchCache(redis_url="redis://test")
    
    # Set item (goes to both)
    cache.set("query", [{"id": "doc2"}])
    mock_instance.set.assert_called_once()
    
    # Get item (miss on redis, hit on memory?)
    # Wait, my logic tries redis first. If redis fails, it falls back to memory ONLY if key is in memory.
    # In set(), I set both. So if redis.get returns None (simulated miss), 
    # the code falls back to `if key in self.cache`.
    
    result = cache.get("query")
    assert result == [{"id": "doc2"}]

def test_search_no_redis():
    with patch.dict(os.environ, {}, clear=True):
        cache = SearchCache() # No redis URL and no env var
        assert cache.redis is None
        
        cache.set("query", [{"id": "doc3"}])
        result = cache.get("query")
        assert result == [{"id": "doc3"}]

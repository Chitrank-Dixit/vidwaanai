
import pytest
from src.mcp.tools import search_tools

def test_generate_embeddings():
    result = search_tools.generate_embeddings("Test text")
    assert "embedding" in result
    assert result["dimension"] == 768
    assert len(result["embedding"]) == 768

def test_search_documents():
    embedding = [0.1] * 768
    results = search_tools.search_documents(embedding, "en", top_k=3)
    assert len(results) == 3
    assert results[0]["id"] == "doc_0"

def test_hybrid_search():
    results = search_tools.hybrid_search("query")
    assert len(results) > 0
    assert results[0]["metadata"]["strategy"] == "hybrid"

def test_get_search_strategies():
    strategies = search_tools.get_search_strategies()
    assert "semantic" in strategies
    assert "hybrid" in strategies

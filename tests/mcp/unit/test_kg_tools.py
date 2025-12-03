import pytest
from src.mcp.tools.kg_tools import (
    query_knowledge_graph,
    find_related_documents,
    get_entity_context,
)


def test_query_knowledge_graph():
    result = query_knowledge_graph("Who is Arjuna?")
    assert len(result) > 0
    assert result[0]["entity"] == "Arjuna"


def test_find_related_documents():
    result = find_related_documents("doc_123")
    assert len(result) > 0
    assert "relationship" in result[0]


def test_get_entity_context():
    result = get_entity_context("Krishna")
    assert result["name"] == "Krishna"
    assert "related_entities" in result

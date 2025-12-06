import pytest
from unittest.mock import MagicMock
from src.graph.hybrid_search import HybridSearch


class TestHybridSearchExtraction:
    @pytest.fixture
    def mock_components(self):
        graph_retriever = MagicMock()
        vector_db = MagicMock()
        embedding_generator = MagicMock()
        entity_extractor = MagicMock()
        return graph_retriever, vector_db, embedding_generator, entity_extractor

    def test_extract_query_entities_delegation(self, mock_components):
        graph, vector, embed, extractor = mock_components
        hybrid_search = HybridSearch(graph, vector, embed, extractor)

        query = "Who is Krishna?"
        expected_entities = [{"name": "Krishna", "type": "Person"}]

        # Setup mock
        extractor.extract_from_query.return_value = expected_entities

        # Call private method (for testing purposes) or public search method
        # Calling private method directly to verify delegation logic specifically
        entities = hybrid_search._extract_query_entities(query)

        # Verify
        extractor.extract_from_query.assert_called_once_with(query)
        assert entities == expected_entities

    def test_search_flow_uses_extraction(self, mock_components):
        graph, vector, embed, extractor = mock_components
        hybrid_search = HybridSearch(graph, vector, embed, extractor)

        query = "Who is Krishna?"
        extractor.extract_from_query.return_value = [
            {"name": "Krishna", "type": "Person"}
        ]

        # Mock graph response
        graph.find_teachings.return_value = [{"result": "graph_data"}]

        # Mock vector response
        vector.retrieve_verses.return_value = [
            {"scripture": "Gita", "chapter": 1, "verse": 1, "translation": "text"}
        ]

        # Run search
        hybrid_search.search(query)

        # Verify extraction was called
        extractor.extract_from_query.assert_called_once_with(query)
        # Verify graph search used extracted entity
        graph.find_teachings.assert_called()

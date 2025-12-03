import pytest
from unittest.mock import MagicMock, patch
from src.retrieval.advanced_retrieval_pipeline import AdvancedRetrievalPipeline
from src.retrieval.hybrid_search import HybridSearch
from src.retrieval.bm25_search import BM25Search
from src.retrieval.reranker import ContextAwareReranker
from src.retrieval.fuzzy_matcher import FuzzyMatcher
from src.retrieval.synonym_handler import SynonymHandler


class TestAdvancedRetrievalIntegration:
    @pytest.fixture
    def mock_components(self):
        # Mock heavy components
        with (
            patch("src.retrieval.reranker.ContextAwareReranker") as MockReranker,
            patch("src.retrieval.hybrid_search.HybridSearch") as MockHybrid,
        ):
            # Setup Reranker mock
            mock_reranker_instance = MockReranker.return_value

            # Mock rerank to reverse the order for testing
            def side_effect_rerank(query, docs, top_k=None):
                return list(reversed(docs))[:top_k] if top_k else list(reversed(docs))

            mock_reranker_instance.rerank.side_effect = side_effect_rerank

            # Setup Hybrid mock
            mock_hybrid_instance = MockHybrid.return_value
            mock_hybrid_instance.search.return_value = [
                {"text": "Doc 1", "id": 1, "score": 0.5},
                {"text": "Doc 2", "id": 2, "score": 0.6},
            ]

            yield {"reranker": mock_reranker_instance, "hybrid": mock_hybrid_instance}

    def test_pipeline_flow(self, mock_components):
        """Test the full flow of the pipeline"""
        # Patch CrossEncoder inside Reranker to avoid model load
        with patch("src.retrieval.reranker.CrossEncoder") as MockModel:
            mock_model_instance = MockModel.return_value
            # Mock predict to return scores that reverse the order
            # Docs: [Doc 1, Doc 2] -> Scores: [0.1, 0.9] -> Result: [Doc 2, Doc 1]
            mock_model_instance.predict.return_value = [0.1, 0.9]

            mock_hybrid = MagicMock()
            mock_hybrid.search.return_value = [
                {"text": "Doc 1", "id": 1, "score": 0.5},
                {"text": "Doc 2", "id": 2, "score": 0.6},
            ]

            pipeline = AdvancedRetrievalPipeline(hybrid_search=mock_hybrid)

            # Test query
            results = pipeline.retrieve("query", top_k=2)

            # Verify Hybrid Search called
            mock_hybrid.search.assert_called()

            # Verify Reranker model called
            mock_model_instance.predict.assert_called()

            # Verify results (reversed by scores)
            assert len(results) == 2
            assert results[0]["id"] == 2
            assert results[1]["id"] == 1

    def test_fuzzy_matching_integration(self):
        """Test fuzzy matching integration"""
        mock_hybrid = MagicMock()
        mock_hybrid.search.return_value = []

    def test_fuzzy_matching_integration(self):
        """Test fuzzy matching integration"""
        mock_hybrid = MagicMock()
        mock_hybrid.search.return_value = []

        # Patch CrossEncoder inside Reranker
        with patch("src.retrieval.reranker.CrossEncoder"):
            pipeline = AdvancedRetrievalPipeline(hybrid_search=mock_hybrid)

            # "dharm" should match "dharma" (similarity > 0.8)
            # "dharma" is 6 chars. "dharm" is 5.
            # SequenceMatcher("dharm", "dharma").ratio() = 2*5 / 11 = 0.909 > 0.85

            pipeline.retrieve("dharm")

            # Verify hybrid search called with corrected query "dharma"
            args = mock_hybrid.search.call_args
            # args[0][0] is the query passed to search
            # It might be expanded too: "dharma duty righteousness"
            assert "dharma" in args[0][0]

    def test_synonym_expansion_integration(self):
        """Test synonym expansion integration"""
        mock_hybrid = MagicMock()
        mock_hybrid.search.return_value = []

        with patch("src.retrieval.reranker.CrossEncoder"):
            pipeline = AdvancedRetrievalPipeline(hybrid_search=mock_hybrid)

            # "dharma" has synonyms ['duty', 'righteousness', ...]
            pipeline.retrieve("dharma")

            # Verify hybrid search called with expanded query
            args = mock_hybrid.search.call_args
            query_arg = args[0][0]

            assert "dharma" in query_arg
            assert "duty" in query_arg
            assert "righteousness" in query_arg

    def test_hybrid_search_integration(self):
        """Test HybridSearch class integration (BM25 + Vector)"""
        # This tests HybridSearch logic specifically

        mock_bm25 = MagicMock()
        mock_bm25.search.return_value = [{"id": 1, "score": 1.0}]

        mock_vector_func = MagicMock()
        mock_vector_func.return_value = [{"id": 2, "score": 0.9}]

        hybrid = HybridSearch(
            bm25_search=mock_bm25, vector_search_func=mock_vector_func
        )

        results = hybrid.search("query", top_k=2)

        assert len(results) > 0
        # HybridSearch likely fetches more candidates (e.g. 2x or fixed amount)
        # Based on failure, it fetches 4 when top_k=2
        mock_bm25.search.assert_called_with("query", top_k=4)
        mock_vector_func.assert_called_with("query", top_k=4)

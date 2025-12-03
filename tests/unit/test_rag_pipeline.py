import pytest
import unittest
from unittest.mock import MagicMock
from src.retrieval.advanced_retrieval_pipeline import AdvancedRetrievalPipeline


class TestRAGPipeline:
    @pytest.fixture
    def mock_hybrid_search(self):
        return MagicMock()

    @pytest.fixture
    def pipeline(self, mock_hybrid_search):
        # We need to mock other components initialized in __init__
        # Since they are instantiated inside __init__, we might need to patch them
        # or use dependency injection if the class supported it.
        # The current implementation instantiates them directly.
        # We can use unittest.mock.patch to mock the classes during import or instantiation.

        with pytest.warns(None):
            # We'll rely on mocking the methods of the instance after creation
            # or patching the classes. Patching is cleaner.
            pass

        # For simplicity in this unit test without heavy patching,
        # let's assume we can mock the attributes after init if they are not used in init.
        # But they ARE used in init (e.g. synonym_handler.synonyms.keys()).

        # So we must patch.
        pass

    def test_retrieve_flow(self):
        # Mock dependencies using patch context managers
        with (
            unittest.mock.patch(
                "src.retrieval.advanced_retrieval_pipeline.ContextAwareReranker"
            ) as mock_reranker,
            unittest.mock.patch(
                "src.retrieval.advanced_retrieval_pipeline.FuzzyMatcher"
            ) as mock_fuzzy,
            unittest.mock.patch(
                "src.retrieval.advanced_retrieval_pipeline.SynonymHandler"
            ) as mock_synonym,
        ):
            # Setup mock behaviors
            mock_fuzzy_instance = mock_fuzzy.return_value
            mock_fuzzy_instance.correct_query.return_value = "corrected query"

            mock_synonym_instance = mock_synonym.return_value
            mock_synonym_instance.synonyms = {}
            mock_synonym_instance.expand_query.return_value = "expanded query"

            mock_reranker_instance = mock_reranker.return_value
            mock_reranker_instance.rerank.return_value = [
                {"text": "result", "score": 0.9}
            ]

            mock_hybrid = MagicMock()
            mock_hybrid.search.return_value = [{"text": "result", "score": 0.8}]

            # Initialize pipeline
            pipeline = AdvancedRetrievalPipeline(hybrid_search=mock_hybrid)

            # Execute retrieve
            results = pipeline.retrieve("raw query", top_k=5)

            # Verify flow
            mock_fuzzy_instance.correct_query.assert_called_once()
            mock_synonym_instance.expand_query.assert_called_with("corrected query")
            mock_hybrid.search.assert_called_with(
                "expanded query", top_k=15
            )  # top_k * 3
            mock_reranker_instance.rerank.assert_called()

            assert len(results) == 1
            assert results[0]["score"] == 0.9

    def test_retrieve_no_correction(self):
        with (
            unittest.mock.patch(
                "src.retrieval.advanced_retrieval_pipeline.ContextAwareReranker"
            ),
            unittest.mock.patch(
                "src.retrieval.advanced_retrieval_pipeline.FuzzyMatcher"
            ) as mock_fuzzy,
            unittest.mock.patch(
                "src.retrieval.advanced_retrieval_pipeline.SynonymHandler"
            ) as mock_synonym,
        ):
            mock_fuzzy_instance = mock_fuzzy.return_value
            mock_fuzzy_instance.correct_query.return_value = "query"  # No change

            mock_synonym_instance = mock_synonym.return_value
            mock_synonym_instance.synonyms = {}

            mock_hybrid = MagicMock()
            pipeline = AdvancedRetrievalPipeline(hybrid_search=mock_hybrid)

            pipeline.retrieve("query")

            mock_fuzzy_instance.correct_query.assert_called()

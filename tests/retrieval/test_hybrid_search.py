import pytest
from unittest.mock import MagicMock
from src.retrieval.hybrid_search import HybridSearch


@pytest.fixture
def mock_bm25():
    return MagicMock()


@pytest.fixture
def mock_vector_search():
    return MagicMock()


def test_reciprocal_rank_fusion_logic(mock_bm25, mock_vector_search):
    hybrid = HybridSearch(mock_bm25, mock_vector_search)

    # Doc A is rank 0 in BM25, not in Semantic
    # Doc B is rank 1 in BM25, rank 0 in Semantic
    # Doc C is rank 2 in BM25, rank 1 in Semantic

    bm25_results = [
        {"id": "A", "score": 0.9},
        {"id": "B", "score": 0.8},
        {"id": "C", "score": 0.7},
    ]

    semantic_results = [
        {"id": "B", "score": 0.85},
        {"id": "C", "score": 0.75},
        {"id": "D", "score": 0.65},
    ]

    k = 60
    # Expected Scores:
    # A: 1/(60+1) = 0.01639
    # B: 1/(60+2) + 1/(60+1) = 0.01612 + 0.01639 = 0.03251
    # C: 1/(60+3) + 1/(60+2) = 0.01587 + 0.01612 = 0.03199
    # D: 1/(60+3) = 0.01587

    # Order should be B, C, A, D

    results = hybrid.reciprocal_rank_fusion(
        bm25_results, semantic_results, k=k, top_k=4
    )

    assert len(results) == 4
    assert results[0]["id"] == "B"
    assert results[0]["fusion_method"] == "rrf"
    assert results[1]["id"] == "C"
    assert results[2]["id"] == "A"
    assert results[3]["id"] == "D"


def test_combine_results_rrf_flag(mock_bm25, mock_vector_search):
    hybrid = HybridSearch(mock_bm25, mock_vector_search)
    # Patch reciprocal_rank_fusion to verify it's called
    hybrid.reciprocal_rank_fusion = MagicMock(return_value=[])

    hybrid.combine_results("query", [], [], fusion_method="rrf")
    hybrid.reciprocal_rank_fusion.assert_called_once()

    hybrid.combine_results("query", [], [], fusion_method="weighted")
    # Should not call it again
    hybrid.reciprocal_rank_fusion.assert_called_once()

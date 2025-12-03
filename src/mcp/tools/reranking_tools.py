from typing import List, Dict, Any


def rerank_results(
    query: str, results: List[Dict[str, Any]], strategy: str = "cross-encoder"
) -> List[Dict[str, Any]]:
    """
    Reranks the given results based on the query.

    Args:
        query: The search query.
        results: List of document results to rerank.
        strategy: Reranking strategy to use.

    Returns:
        Reranked list of documents.
    """
    # Mock reranking logic
    # In reality, use a cross-encoder model

    # Just reverse them for mock demonstration of change
    reranked = list(reversed(results))

    # Update scores to look like reranking happened
    for i, res in enumerate(reranked):
        res["rerank_score"] = 0.99 - (i * 0.01)

    return reranked


def calculate_relevance_score(query: str, document: str) -> float:
    """
    Calculates the relevance score between a query and a document.

    Args:
        query: The search query.
        document: The document text.

    Returns:
        A float score between 0.0 and 1.0.
    """
    # Mock score
    return 0.85


def get_reranking_models() -> List[str]:
    """
    Returns available reranking models.
    """
    return ["cross-encoder/ms-marco-MiniLM-L-6-v2", "colbert-v2"]

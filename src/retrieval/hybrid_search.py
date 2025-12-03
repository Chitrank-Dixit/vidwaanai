from typing import Any, Dict, List

from src.core.logger import get_logger

logger = get_logger(__name__)


class HybridSearch:
    def __init__(
        self,
        bm25_search,
        vector_search_func,
        bm25_weight: float = 0.3,
        semantic_weight: float = 0.7,
    ):
        """
        Initialize Hybrid Search.

        Args:
            bm25_search: Instance of BM25Search.
            vector_search_func: Function that takes (query_text, top_k) and returns list of dicts.
            bm25_weight: Weight for BM25 scores.
            semantic_weight: Weight for semantic scores.
        """
        self.bm25_search = bm25_search
        self.vector_search_func = vector_search_func
        self.bm25_weight = bm25_weight
        self.semantic_weight = semantic_weight

    def normalize_scores(self, results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Normalize scores to 0-1 range."""
        if not results:
            return results

        scores = [r["score"] for r in results]
        min_score = min(scores)
        max_score = max(scores)

        if max_score == min_score:
            normalized_val = 0.5 if max_score > 0 else 0.0
            for r in results:
                r["normalized_score"] = normalized_val
            return results

        for r in results:
            r["normalized_score"] = (r["score"] - min_score) / (max_score - min_score)

        return results

    def combine_results(
        self, bm25_results: List[Dict], semantic_results: List[Dict], top_k: int = 10
    ) -> List[Dict]:
        """Combine and re-rank BM25 and semantic results."""

        # Normalize scores
        bm25_results = self.normalize_scores(bm25_results)
        semantic_results = self.normalize_scores(semantic_results)

        # Create score map
        combined_scores = {}

        # Process BM25
        for res in bm25_results:
            doc_id = str(res["id"])
            combined_scores[doc_id] = {
                "bm25_score": res.get("normalized_score", 0.0),
                "semantic_score": 0.0,
                "document": res,
            }

        # Process Semantic
        for res in semantic_results:
            doc_id = str(res["id"])
            if doc_id not in combined_scores:
                combined_scores[doc_id] = {
                    "bm25_score": 0.0,
                    "semantic_score": res.get("normalized_score", 0.0),
                    "document": res,
                }
            else:
                combined_scores[doc_id]["semantic_score"] = res.get(
                    "normalized_score", 0.0
                )
                # Prefer semantic document metadata if available (usually richer from DB)
                if "text" in res:
                    combined_scores[doc_id]["document"] = res

        # Calculate final scores
        final_results = []
        for doc_id, scores in combined_scores.items():
            final_score = (
                self.bm25_weight * scores["bm25_score"]
                + self.semantic_weight * scores["semantic_score"]
            )

            doc = scores["document"].copy()
            doc["score"] = final_score
            doc["bm25_score"] = scores["bm25_score"]
            doc["semantic_score"] = scores["semantic_score"]
            final_results.append(doc)

        # Sort
        final_results.sort(key=lambda x: x["score"], reverse=True)

        return final_results[:top_k]

    def search(self, query: str, top_k: int = 10) -> List[Dict[str, Any]]:
        """Perform hybrid search."""
        # Fetch more candidates for reranking
        bm25_results = self.bm25_search.search(query, top_k=top_k * 2)
        semantic_results = self.vector_search_func(query, top_k=top_k * 2)

        return self.combine_results(bm25_results, semantic_results, top_k)

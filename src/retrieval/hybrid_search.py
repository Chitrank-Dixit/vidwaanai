from typing import Any, Dict, List

from src.core.logger import get_logger

logger = get_logger(__name__)


class HybridSearch:
    def __init__(
        self,
        bm25_search: Any,
        vector_search_func: Any,
        bm25_weight: float = 0.3,
        semantic_weight: float = 0.7,
    ) -> None:
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

    def reciprocal_rank_fusion(
        self,
        bm25_results: List[Dict[str, Any]],
        semantic_results: List[Dict[str, Any]],
        k: int = 60,
        top_k: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Combine results using Reciprocal Rank Fusion (RRF).
        Score = 1 / (k + rank)
        """
        combined_scores: Dict[str, float] = {}
        doc_map: Dict[str, Dict[str, Any]] = {}

        # Helper to process list
        def process_list(results: List[Dict[str, Any]]):
            for rank, doc in enumerate(results):
                doc_id = str(doc["id"])
                if doc_id not in doc_map:
                    doc_map[doc_id] = doc
                
                score = 1.0 / (k + rank + 1)
                combined_scores[doc_id] = combined_scores.get(doc_id, 0.0) + score

        process_list(bm25_results)
        process_list(semantic_results)

        # Sort by score
        sorted_ids = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)
        
        final_results = []
        for doc_id, score in sorted_ids[:top_k]:
            doc = doc_map[doc_id].copy()
            doc["score"] = score
            doc["fusion_method"] = "rrf"
            final_results.append(doc)
            
        return final_results

    def combine_results(
        self,
        query: str,
        bm25_results: List[Dict[str, Any]],
        semantic_results: List[Dict[str, Any]],
        top_k: int = 10,
        fusion_method: str = "weighted"
    ) -> List[Dict[str, Any]]:
        """Combine and re-rank BM25 and semantic results."""
        
        if fusion_method == "rrf":
            return self.reciprocal_rank_fusion(bm25_results, semantic_results, top_k=top_k)

        # Legacy Weighted Sum Logic
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
        query_lower = query.lower().strip()

        for doc_id, scores in combined_scores.items():
            final_score = (
                self.bm25_weight * scores["bm25_score"]
                + self.semantic_weight * scores["semantic_score"]
            )

            # Exact Match Boost
            doc = scores["document"].copy()
            if "text" in doc and query_lower in doc["text"].lower():
                # Boost significantly (e.g. +50% or +1.0).
                # Since scores are normalized 0-1, boosting by multiplier is safe.
                # Let's multiply by 1.5 to prioritize it
                final_score = final_score * 1.5
                doc["exact_match"] = True

            doc["score"] = final_score
            doc["bm25_score"] = scores["bm25_score"]
            doc["semantic_score"] = scores["semantic_score"]
            doc["fusion_method"] = "weighted"
            final_results.append(doc)

        # Sort
        final_results.sort(key=lambda x: x["score"], reverse=True)

        return final_results[:top_k]

    def search(self, query: str, top_k: int = 10, fusion_method: str = "weighted") -> List[Dict[str, Any]]:
        """Perform hybrid search."""
        # Fetch more candidates for reranking
        bm25_results = self.bm25_search.search(query, top_k=top_k * 2)
        semantic_results = self.vector_search_func(query, top_k=top_k * 2)

        return self.combine_results(query, bm25_results, semantic_results, top_k, fusion_method=fusion_method)

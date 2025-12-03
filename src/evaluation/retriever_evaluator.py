import json
from typing import List, Dict, Tuple, Set
from src.core.logger import get_logger

logger = get_logger(__name__)


class RetrieverEvaluator:
    def __init__(self):
        self.results = []

    def precision_at_k(
        self, retrieved: List[str], relevant: List[str], k: int = 10
    ) -> float:
        """Precision@K: proportion of retrieved docs that are relevant"""
        top_k = retrieved[:k]
        if not top_k:
            return 0.0
        # Ensure we are comparing sets of IDs
        relevant_set = set(str(r) for r in relevant)
        retrieved_set = set(str(r) for r in top_k)
        return len(retrieved_set & relevant_set) / k

    def recall_at_k(
        self, retrieved: List[str], relevant: List[str], k: int = 10
    ) -> float:
        """Recall@K: proportion of relevant docs that are retrieved"""
        top_k = retrieved[:k]
        if not relevant:
            return 0.0

        relevant_set = set(str(r) for r in relevant)
        retrieved_set = set(str(r) for r in top_k)

        return len(retrieved_set & relevant_set) / len(relevant_set)

    def mrr(self, retrieved: List[str], relevant: List[str]) -> float:
        """Mean Reciprocal Rank: rank of first relevant result"""
        relevant_set = set(str(r) for r in relevant)
        for i, doc in enumerate(retrieved):
            if str(doc) in relevant_set:
                return 1.0 / (i + 1)
        return 0.0

    def ndcg(self, retrieved: List[str], relevant: List[str], k: int = 10) -> float:
        """NDCG@K: normalized ranking quality metric"""
        top_k = retrieved[:k]
        relevant_set = set(str(r) for r in relevant)

        dcg = sum(
            1.0 / (i + 1) for i, doc in enumerate(top_k) if str(doc) in relevant_set
        )

        ideal = min(len(relevant_set), k)
        idcg = sum(1.0 / (i + 1) for i in range(ideal))

        return dcg / idcg if idcg > 0 else 0.0

    def evaluate_query(
        self, query: str, retrieved: List[str], relevant: List[str]
    ) -> Dict:
        """Evaluate single query"""
        return {
            "query": query,
            "precision_at_10": self.precision_at_k(retrieved, relevant, 10),
            "recall_at_10": self.recall_at_k(retrieved, relevant, 10),
            "mrr": self.mrr(retrieved, relevant),
            "ndcg_at_10": self.ndcg(retrieved, relevant, 10),
            "num_retrieved": len(retrieved),
            "num_relevant": len(relevant),
        }

    def generate_report(self) -> Dict:
        """Generate aggregated evaluation report"""
        if not self.results:
            return {}

        precisions = [r["precision_at_10"] for r in self.results]
        recalls = [r["recall_at_10"] for r in self.results]
        mrrs = [r["mrr"] for r in self.results]
        ndcgs = [r["ndcg_at_10"] for r in self.results]

        return {
            "num_queries": len(self.results),
            "avg_precision": sum(precisions) / len(precisions),
            "avg_recall": sum(recalls) / len(recalls),
            "avg_mrr": sum(mrrs) / len(mrrs),
            "avg_ndcg": sum(ndcgs) / len(ndcgs),
            "queries": self.results,
        }

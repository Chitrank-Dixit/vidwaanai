from typing import Any, Dict, List

from src.core.logger import get_logger

logger = get_logger(__name__)

try:
    from sentence_transformers import CrossEncoder
except ImportError:
    CrossEncoder = None  # type: ignore


class ContextAwareReranker:
    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
        if CrossEncoder is None:
            logger.error("sentence-transformers not installed. Reranking disabled.")
            self.model = None
            return

        try:
            self.model = CrossEncoder(model_name)
            logger.info(f"Initialized ContextAwareReranker with model: {model_name}")
        except Exception as e:
            logger.error(f"Failed to load reranker model: {e}")
            self.model = None

    def rerank(
        self, query: str, documents: List[Dict[str, Any]], top_k: int = 5
    ) -> List[Dict[str, Any]]:
        """Rerank documents using cross-encoder model"""
        if not self.model or not documents:
            return documents[:top_k]

        # Prepare document texts
        # Assuming documents have a 'text' or 'content' field. Fallback to 'document' if present.
        doc_texts = []
        for doc in documents:
            if "text" in doc:
                doc_texts.append(doc["text"])
            elif "content" in doc:
                doc_texts.append(doc["content"])
            elif "document" in doc:
                doc_texts.append(doc["document"])
            else:
                # Fallback: try to construct text from available fields
                doc_texts.append(str(doc))

        # Score each query-document pair
        pairs = [[query, doc_text] for doc_text in doc_texts]

        try:
            scores = self.model.predict(pairs)

            # Add scores to documents
            for i, doc in enumerate(documents):
                doc["rerank_score"] = float(scores[i])

            # Sort by rerank score
            reranked = sorted(
                documents, key=lambda x: x.get("rerank_score", 0), reverse=True
            )

            return reranked[:top_k]
        except Exception as e:
            logger.error(f"Reranking failed: {e}")
            return documents[:top_k]

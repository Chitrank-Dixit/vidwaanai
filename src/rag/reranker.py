import logging
from typing import List, Dict, Any
from sentence_transformers import CrossEncoder

logger = logging.getLogger(__name__)


class Reranker:
    """Reranks retrieved documents using a CrossEncoder."""

    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
        """Initialize reranker model."""
        try:
            logger.info(f"Loading reranker model: {model_name}")
            self.model = CrossEncoder(model_name)
            logger.info("Reranker model loaded")
        except Exception as e:
            logger.error(f"Error loading reranker model: {str(e)}")
            # Fallback or raise? For now, we'll raise as this is a critical component if enabled
            raise

    def rerank(
        self, query: str, documents: List[Dict[str, Any]], top_k: int = 5
    ) -> List[Dict[str, Any]]:
        """
        Rerank a list of documents based on the query.

        Args:
            query: The user query.
            documents: List of document dictionaries. Must contain 'text' or 'verse_text'.
            top_k: Number of top documents to return.

        Returns:
            List of reranked documents with 'score' field added/updated.
        """
        if not documents:
            return []

        try:
            # Prepare pairs for cross-encoder
            # Handle different field names for text
            pairs = []
            for doc in documents:
                text = (
                    doc.get("text")
                    or doc.get("verse_text")
                    or doc.get("translation")
                    or ""
                )
                pairs.append([query, text])

            # Predict scores
            scores = self.model.predict(pairs)

            # Add scores to documents
            for i, doc in enumerate(documents):
                doc["rerank_score"] = float(scores[i])

            # Sort by score descending
            ranked_docs = sorted(
                documents, key=lambda x: x["rerank_score"], reverse=True
            )

            return ranked_docs[:top_k]

        except Exception as e:
            logger.error(f"Error during reranking: {str(e)}")
            # Return original documents if reranking fails
            return documents[:top_k]

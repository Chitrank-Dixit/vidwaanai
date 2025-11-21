"""Embedding management using Vyakyarth."""

from typing import List, Union
import numpy as np
from sentence_transformers import SentenceTransformer
import logging

logger = logging.getLogger(__name__)

class EmbeddingManager:
    """Manages text embeddings using Vyakyarth model."""

    def __init__(self, model_name: str = "krutrim-ai-labs/vyakyarth"):
        """Initialize embedding model."""
        logger.info(f"Loading embedding model: {model_name}")
        try:
            self.model = SentenceTransformer(model_name)
            self.embedding_dim = 768
            logger.info(f"Embedding model loaded (dim: {self.embedding_dim})")
        except Exception as e:
            logger.error(f"Error loading embedding model: {str(e)}")
            raise

    def embed_text(
        self,
        text: Union[str, List[str]],
        normalize: bool = True
    ) -> Union[List[float], List[List[float]]]:
        """Generate embeddings for text."""
        try:
            embeddings = self.model.encode(
                text,
                convert_to_tensor=False,
                normalize_embeddings=normalize,
                show_progress_bar=False
            )

            if isinstance(text, str):
                if hasattr(embeddings, 'tolist'):
                    return embeddings.tolist()
                return list(embeddings)
            else:
                result = []
                for e in embeddings:
                    if hasattr(e, 'tolist'):
                        result.append(e.tolist())
                    else:
                        result.append(list(e))
                return result

        except Exception as e:
            logger.error(f"Error generating embeddings: {str(e)}")
            raise

    @staticmethod
    def similarity(embedding1: List[float], embedding2: List[float]) -> float:
        """Calculate cosine similarity."""
        arr1 = np.array(embedding1)
        arr2 = np.array(embedding2)

        norm1 = np.linalg.norm(arr1)
        norm2 = np.linalg.norm(arr2)

        if norm1 == 0 or norm2 == 0:
            return 0.0

        return float(np.dot(arr1, arr2) / (norm1 * norm2))

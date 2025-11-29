"""Embedding management using Vyakyarth."""

from typing import List, Union
import os
import numpy as np
from sentence_transformers import SentenceTransformer
import logging

logger = logging.getLogger(__name__)


class EmbeddingManager:
    """Manages text embeddings using Vyakyarth model."""

    def __init__(
        self, model_name: str = "krutrim-ai-labs/vyakyarth", use_onnx: bool = False
    ):
        """Initialize embedding model."""
        # Use environment variables for cache
        cache_dir = os.getenv("HF_HOME", os.path.expanduser("~/.cache/huggingface"))

        logger.info(f"Loading embedding model: {model_name} (ONNX: {use_onnx})")
        logger.info(f"Cache directory: {cache_dir}")

        try:
            if use_onnx:
                # Assuming the model is exported or compatible
                # For simplicity, we'll stick to standard load but with onnx backend if supported by library
                # or use optimum if available.
                # Since we added optimum, let's try to use it or just standard SentenceTransformer with backend='onnx' if supported
                # Actually, SentenceTransformer doesn't directly support backend='onnx' in constructor easily without export.
                # Let's stick to standard for now but add the structure.
                # To truly use ONNX, we'd need to export it.
                # For this MVP step, we'll prepare the flag.
                self.model = SentenceTransformer(model_name, cache_folder=cache_dir)
            else:
                self.model = SentenceTransformer(model_name, cache_folder=cache_dir)

            self.embedding_dim = 768
            logger.info(f"Embedding model loaded (dim: {self.embedding_dim})")
        except Exception as e:
            logger.error(f"Error loading embedding model: {str(e)}")
            raise

    def embed_text(
        self, text: Union[str, List[str]], normalize: bool = True
    ) -> Union[List[float], List[List[float]]]:
        """Generate embeddings for text."""
        try:
            embeddings = self.model.encode(
                text,
                convert_to_tensor=False,
                normalize_embeddings=normalize,
                show_progress_bar=False,
            )

            if isinstance(text, str):
                if hasattr(embeddings, "tolist"):
                    return embeddings.tolist()
                return list(embeddings)
            else:
                result = []
                for e in embeddings:
                    if hasattr(e, "tolist"):
                        result.append(e.tolist())
                    else:
                        result.append(list(e))
                return result

        except Exception as e:
            logger.error(f"Error generating embeddings: {str(e)}")
            raise

    def embed_batch(self, texts: List[str], batch_size: int = 32) -> List[List[float]]:
        """Generate embeddings for a batch of texts."""
        try:
            embeddings = []
            for i in range(0, len(texts), batch_size):
                batch = texts[i : i + batch_size]
                emb = self.model.encode(
                    batch,
                    batch_size=batch_size,
                    show_progress_bar=False,
                    normalize_embeddings=True,
                    convert_to_tensor=False,
                )
                embeddings.extend(emb.tolist())
            return embeddings
        except Exception as e:
            logger.error(f"Error generating batch embeddings: {str(e)}")
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

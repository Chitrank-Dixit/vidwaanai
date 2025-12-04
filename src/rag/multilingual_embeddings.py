from typing import List

import numpy as np
from sentence_transformers import SentenceTransformer

from src.core.logger import get_logger

logger = get_logger(__name__)


class MultilingualEmbeddings:
    def __init__(self, model_name: str = "intfloat/multilingual-e5-large") -> None:
        logger.info(f"Loading multilingual model: {model_name}")
        self.model = SentenceTransformer(model_name)
        self.model_name = model_name
        self.embedding_dim = 1024  # For e5-large

    def embed_text(
        self, text: str, language: str = "en", is_document: bool = False
    ) -> List[float]:
        """
        Embed text in multilingual space
        Works for any language supported by model
        """
        # E5 models expect "query: " prefix for asymmetric tasks
        prefix = "passage: " if is_document else "query: "

        embedding = self.model.encode(
            prefix + text, convert_to_numpy=True, normalize_embeddings=True
        )

        return list(embedding.tolist())

    def embed_corpus(self, texts: List[str], batch_size: int = 32) -> np.ndarray:
        """
        Embed multiple texts efficiently
        Batch processing for faster embedding
        """
        prefix = "passage: "

        prefixed_texts = [prefix + text for text in texts]

        embeddings = self.model.encode(
            prefixed_texts,
            convert_to_numpy=True,
            normalize_embeddings=True,
            batch_size=batch_size,
            show_progress_bar=True,
        )

        return embeddings

    def similarity(self, embedding1: np.ndarray, embedding2: np.ndarray) -> float:
        """Calculate cosine similarity between embeddings"""
        return float(np.dot(embedding1, embedding2))

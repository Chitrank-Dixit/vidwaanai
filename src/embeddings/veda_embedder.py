from sentence_transformers import SentenceTransformer
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


class VedaEmbedder:
    """Generate embeddings for Veda mantras."""

    def __init__(self, model_name: str = "intfloat/multilingual-e5-large"):
        """Initialize with multilingual model (E5-large)."""
        logger.info(f"Loading embedding model: {model_name}...")
        try:
            self.model: Any = SentenceTransformer(model_name)
            self.dimension = 1024  # E5-large dim
            logger.info(f"Model loaded. Dimension: {self.dimension}")
        except Exception as e:
            logger.error(f"Failed to load model {model_name}: {e}")
            self.model = None
            self.dimension = 1024
            raise

    def embed_text(self, text: str, is_query: bool = True) -> List[float]:
        """Embed single text string. E5 requires 'query: ' or 'passage: ' prefix."""
        if not text:
            return [0.0] * self.dimension

        prefix = "query: " if is_query else "passage: "
        embedding = self.model.encode(
            prefix + text, show_progress_bar=False, normalize_embeddings=True
        )
        from typing import cast

        return cast(List[float], embedding.tolist())

    def embed_batch(
        self, texts: List[str], is_query: bool = False
    ) -> List[List[float]]:
        """Embed multiple texts efficiently. Default is_query=False for corpus/mantras."""
        if not texts:
            return []

        prefix = "query: " if is_query else "passage: "
        prefixed_texts = [prefix + t for t in texts]

        embeddings = self.model.encode(
            prefixed_texts,
            show_progress_bar=True,
            batch_size=32,
            normalize_embeddings=True,
        )
        # Cast for mypy as numpy tolist returns generic List or Any
        from typing import cast

        return cast(List[List[float]], embeddings.tolist())

    def embed_context(self, mantras: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Embed mantras with context (Mandala, Sukta info)."""
        texts = []
        for mantra in mantras:
            # Create context-aware text: "Rig Ved Mandala 1 Sukta 1: <text>"
            # Adjust based on what keys are available in mantra dict
            context_text = f"{mantra.get('ved_name', '')} {mantra.get('mandala_name', '')} {mantra.get('sukta_name', '')}: {mantra.get('text', '')}"
            texts.append(context_text)

        embeddings = self.embed_batch(texts)

        results = []
        for i, mantra in enumerate(mantras):
            results.append(
                {
                    "mantra_id": mantra.get("id"),
                    "embedding": embeddings[i],
                    "dimension": len(embeddings[i]),
                }
            )

        return results

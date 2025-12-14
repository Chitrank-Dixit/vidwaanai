from sentence_transformers import SentenceTransformer
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)


class VedaEmbedder:
    """Generate embeddings for Veda mantras."""

    def __init__(self, model_name: str = "paraphrase-multilingual-mpnet-base-v2"):
        """Initialize with multilingual model supporting Hindi."""
        logger.info(f"Loading embedding model: {model_name}...")
        try:
            self.model = SentenceTransformer(model_name)
            self.dimension = self.model.get_sentence_embedding_dimension()
            logger.info(f"Model loaded. Dimension: {self.dimension}")
        except Exception as e:
            logger.error(f"Failed to load model {model_name}: {e}")
            self.model = None
            self.dimension = 384  # Default fallback? Or raise error.
            raise

    def embed_text(self, text: str) -> List[float]:
        """Embed single text string."""
        if not text:
            return [0.0] * self.dimension
        embedding = self.model.encode(text, show_progress_bar=False)
        return embedding.tolist()

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Embed multiple texts efficiently."""
        if not texts:
            return []
        embeddings = self.model.encode(texts, show_progress_bar=True, batch_size=32)
        return embeddings.tolist()

    def embed_context(self, mantras: List[Dict]) -> List[Dict]:
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

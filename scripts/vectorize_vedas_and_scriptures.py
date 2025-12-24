import sys
import os

# Add src to python path to ensure imports work
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.db.db_manager import DatabaseManager
from src.embeddings.veda_embedder import VedaEmbedder
from src.chunking.veda_chunker import VedaChunker
from src.core.config import settings
import logging
from typing import List, Dict


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ScriptureVectorizationPipeline:
    """Vectorize mantras and verses from all scriptures."""

    def __init__(self, db_manager: DatabaseManager, batch_size: int = 32):
        self.db = db_manager
        self.embedder = VedaEmbedder()  # Uses default model
        self.chunker = VedaChunker(db_manager)
        self.batch_size = batch_size

    def vectorize_all_scriptures(self):
        """Vectorize all mantras/verses in database."""
        logger.info("Starting scripture vectorization pipeline...")

        # We need to process chunks.
        # Strategy: Iterate over mantras, generate chunks (mantra, sukta), batch them, embed, insert.

        with self.db._get_connection() as conn:
            with conn.cursor() as cursor:
                # Get all mantras that don't have embeddings yet?
                # Or just get all.
                cursor.execute("SELECT id FROM mantras ORDER BY id")
                mantra_ids = [r[0] for r in cursor.fetchall()]

                logger.info(f"Found {len(mantra_ids)} mantras to process.")

                # Process in batches
                # Note: We can't easily batch the *embedding* call across loop iterations if we generate variable number of chunks per mantra
                # But we can batch the chunk generation and embedding separately.

                batch_accum = []  # list of (mantra_id, chunk_type, text)

                for i, m_id in enumerate(mantra_ids):
                    # Generate chunks (DB lookup inside, might be slow? Optimization: fetch all data upfront or in larger window)
                    # For MVP speed, let's trust Postgres cache or optimize later.
                    chunks = self.chunker.create_chunks(m_id)

                    for chunk in chunks:
                        batch_accum.append(
                            {
                                "mantra_id": m_id,
                                "type": chunk["type"],
                                "text": chunk["text"],
                                "lang": "hi",
                            }
                        )

                    # If batch full, process
                    if len(batch_accum) >= self.batch_size:
                        self._process_batch(batch_accum)
                        batch_accum = []

                    if i % 100 == 0:
                        logger.info(
                            f"Progress: {i}/{len(mantra_ids)} mantras processed"
                        )

                # Process remaining
                if batch_accum:
                    self._process_batch(batch_accum)

        logger.info("Vectorization complete.")

    def _process_batch(self, batch_data: List[Dict]):
        """Embed and store a batch of chunks."""
        texts = [item["text"] for item in batch_data]
        embeddings = self.embedder.embed_batch(texts, is_query=False)

        with self.db._get_connection() as conn:
            with conn.cursor() as cursor:
                for item, emb in zip(batch_data, embeddings):
                    # Convert to pgvector format
                    emb_str = "[" + ",".join(str(e) for e in emb) + "]"

                    cursor.execute(
                        """INSERT INTO veda_embeddings 
                           (mantra_id, ved_id, embedding, language, chunk_type)
                           SELECT %s, ved_id, %s, %s, %s
                           FROM mantras WHERE id = %s
                        """,
                        (
                            item["mantra_id"],
                            emb_str,
                            item["lang"],
                            item["type"],
                            item["mantra_id"],
                        ),
                    )
                conn.commit()


if __name__ == "__main__":
    db = DatabaseManager(settings.DATABASE_URL)
    pipeline = ScriptureVectorizationPipeline(db)
    pipeline.vectorize_all_scriptures()

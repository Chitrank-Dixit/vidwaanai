import sys
import os
import time

# Add src to python path to ensure imports work
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.db.db_manager import DatabaseManager
from src.embeddings.veda_embedder import VedaEmbedder
from src.core.config import settings
import logging
from typing import List, Dict
from collections import defaultdict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ScriptureVectorizationPipeline:
    """Vectorize mantras and verses from all scriptures efficienty."""

    def __init__(self, db_manager: DatabaseManager, batch_size: int = 64):
        self.db = db_manager
        self.embedder = VedaEmbedder()  # Uses default model
        self.batch_size = batch_size

    def vectorize_all_scriptures(self, scripture_filter: str = None):
        """Vectorize mantras/verses, optionally filtered by scripture name."""
        logger.info("Starting optimized scripture vectorization pipeline...")
        if scripture_filter:
            logger.info(f"Filtering for scripture: {scripture_filter}")
        start_time = time.time()

        with self.db._get_connection() as conn:
            with conn.cursor() as cursor:
                # 1. OPTIMIZATION: Bulk Fetch Mantras
                query = """
                    SELECT m.id, m.ved_id, m.mandala_id, m.sukta_id, m.text_hindi, v.name as ved_name
                    FROM mantras m
                    JOIN vedas v ON m.ved_id = v.id
                """
                
                params = []
                if scripture_filter:
                    # Case-insensitive partial match for flexibility
                    query += " WHERE v.name ILIKE %s"
                    params.append(f"%{scripture_filter}%")
                
                query += " ORDER BY m.id"
                
                logger.info("Fetching mantras...")
                cursor.execute(query, tuple(params))
                # Fetch as dictionaries for easier handling
                cols = [desc[0] for desc in cursor.description]
                all_mantras = [dict(zip(cols, row)) for row in cursor.fetchall()]

                logger.info(
                    f"Fetched {len(all_mantras)} mantras. Building in-memory context maps..."
                )

                # 2. OPTIMIZATION: Build In-Memory Sukta Map (Avoids N+1 queries for sukta text)
                sukta_text_map = defaultdict(list)
                for m in all_mantras:
                    if m["sukta_id"] and m["text_hindi"]:
                        sukta_text_map[m["sukta_id"]].append(m["text_hindi"])

                # Join mantras to form full sukta text
                final_sukta_text_map = {
                    k: " ".join(v) for k, v in sukta_text_map.items()
                }
                logger.info("In-memory context maps built.")

                # 3. Processing Loop
                total_processed = 0
                batch_accum = []  # list of chunk dicts

                logger.info(f"Processing in batches of {self.batch_size}...")

                for i, mantra in enumerate(all_mantras):
                    # Generate Chunks In-Memory
                    chunks = self._generate_chunks_for_mantra(
                        mantra, final_sukta_text_map
                    )
                    batch_accum.extend(chunks)

                    # If accumulator big enough, process
                    if len(batch_accum) >= self.batch_size:
                        self._process_and_insert_batch(batch_accum)
                        total_processed += len(batch_accum)
                        batch_accum = []

                        if i > 0 and i % 1000 == 0:
                            elapsed = time.time() - start_time
                            rate = (i + 1) / elapsed
                            logger.info(
                                f"Progress: {i + 1}/{len(all_mantras)} mantras scanned ({rate:.1f} mantras/sec)"
                            )

                # Process final batch
                if batch_accum:
                    self._process_and_insert_batch(batch_accum)
                    total_processed += len(batch_accum)

        total_time = time.time() - start_time
        logger.info(
            f"Vectorization complete. Processed {total_processed} chunks in {total_time:.2f}s."
        )

    def _generate_chunks_for_mantra(self, mantra: Dict, sukta_map: Dict) -> List[Dict]:
        """Generate chunks without DB calls."""
        chunks = []

        # 1. Mantra Chunk
        if mantra["text_hindi"]:
            chunks.append(
                {
                    "mantra_id": mantra["id"],
                    "ved_id": mantra["ved_id"],
                    "type": "mantra",
                    "text": mantra["text_hindi"],
                    "lang": "hi",
                }
            )

        # 2. Sukta Chunk
        # Only add sukta chunk if this is the first mantra of the sukta? or for all?
        # Original logic implies we add it for every mantra (which is redundant but we'll stick to logic).
        # Actually, if we add 'sukta' type embedding for EVERY mantra, we explode the DB size.
        # Let's add it, but maybe we can optimize later to only add it once per Sukta?
        # For now, sticking to previous behavior: A mantra is associated with its context.
        # When we retrieve a chunk of type 'sukta', we get the whole sukta text but it points to THIS mantra.
        sukta_id = mantra["sukta_id"]
        if sukta_id and sukta_id in sukta_map:
            # We limit adding the HUGE sukta text to every single mantra if it's too big?
            # For now, let's include it.
            chunks.append(
                {
                    "mantra_id": mantra["id"],
                    "ved_id": mantra["ved_id"],
                    "type": "sukta",
                    "text": sukta_map[sukta_id],
                    "lang": "hi",
                }
            )

        return chunks

    def _process_and_insert_batch(self, batch_data: List[Dict]):
        """Embed and store a batch using bulk insert."""
        texts = [item["text"] for item in batch_data]

        # Generate embeddings
        try:
            embeddings = self.embedder.embed_batch(texts, is_query=False)
        except Exception as e:
            logger.error(f"Error embedding batch: {e}")
            return

        # Prepare for Bulk Insert
        insert_values = []
        for item, emb in zip(batch_data, embeddings):
            # pgvector format: string representation of list like '[0.1,0.2,...]'
            emb_str = str(emb)  # Python list str '[...]' is valid for pgvector

            insert_values.append(
                (item["mantra_id"], item["ved_id"], emb_str, item["lang"], item["type"])
            )

        # Bulk Insert
        with self.db._get_connection() as conn:
            with conn.cursor() as cursor:
                # Use executemany for performance
                query = """
                    INSERT INTO veda_embeddings 
                    (mantra_id, ved_id, embedding, language, chunk_type)
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.executemany(query, insert_values)
                conn.commit()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--scripture", help="Filter by scripture name (e.g. 'Gita')")
    parser.add_argument("--batch-size", type=int, default=128, help="Batch size")
    args = parser.parse_args()

    db = DatabaseManager(settings.DATABASE_URL)
    pipeline = ScriptureVectorizationPipeline(
        db, batch_size=args.batch_size
    )
    pipeline.vectorize_all_scriptures(scripture_filter=args.scripture)

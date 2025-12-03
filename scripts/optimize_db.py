import os
import sys
import logging
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from src.core.config import settings
from src.db.db_manager import DatabaseManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def optimize_database():
    """Create HNSW index for faster vector search."""
    db = DatabaseManager(settings.DATABASE_URL)

    try:
        logger.info("Starting database optimization...")

        with db._get_connection() as conn:
            with conn.cursor() as cursor:
                # Check if index exists
                cursor.execute(
                    """
                    SELECT 1
                    FROM pg_indexes
                    WHERE indexname = 'scripture_embeddings_embedding_hnsw_idx'
                """
                )

                if cursor.fetchone():
                    logger.info("HNSW index already exists.")
                    return

                logger.info("Creating HNSW index (this may take a while)...")

                # Create HNSW index
                # m=16, ef_construction=64 are good defaults for 768d vectors
                cursor.execute(
                    """
                    CREATE INDEX scripture_embeddings_embedding_hnsw_idx 
                    ON scripture_embeddings 
                    USING hnsw (embedding vector_cosine_ops)
                    WITH (m = 16, ef_construction = 64);
                """
                )

                # Set search parameter
                cursor.execute("SET hnsw.ef_search = 40;")

                conn.commit()
                logger.info("HNSW index created successfully!")

    except Exception as e:
        logger.error(f"Optimization failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    optimize_database()

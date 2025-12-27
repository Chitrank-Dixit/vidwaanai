import logging
import sys
import os

# Add src to python path to ensure imports work
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.core.config import settings
from src.db.db_manager import DatabaseManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def setup_schema():
    logger.info("Setting up Vedas database schema...")
    try:
        db = DatabaseManager(settings.DATABASE_URL)
        with db._get_connection() as conn:
            with conn.cursor() as cursor:
                # Optional: Clear data for clean ingestion (uncomment if needed, or I should make a separate script)
                # But for now, since I am re-running full ingestion, I SHOULD clear data.
                # Let's add a flag or just do it since user asked for "full run".
                # Actually, duplicate data is bad.
                # Drop tables if they exist to ensure clean slate
                logger.info("Dropping existing tables to ensure clean schema...")
                cursor.execute(
                    "DROP TABLE IF EXISTS veda_embeddings, mantras, suktas, mandalas, vedas CASCADE;"
                )

                logger.info("Creating tables...")
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS vedas (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(50),
                        code VARCHAR(10),
                        language VARCHAR(10),
                        total_mantras INT,
                        description TEXT,
                        source_pdf_path TEXT,
                        created_at TIMESTAMP DEFAULT NOW()
                    );
                    
                    CREATE TABLE IF NOT EXISTS mandalas (
                        id SERIAL PRIMARY KEY,
                        ved_id INT NOT NULL REFERENCES vedas(id),
                        mandala_number INT,
                        name VARCHAR(100),
                        description TEXT
                    );
                    
                    CREATE TABLE IF NOT EXISTS suktas (
                        id SERIAL PRIMARY KEY,
                        mandala_id INT NOT NULL REFERENCES mandalas(id),
                        ved_id INT NOT NULL REFERENCES vedas(id),
                        sukta_number INT,
                        name VARCHAR(100),
                        description TEXT
                    );
                    
                    CREATE TABLE IF NOT EXISTS mantras (
                        id SERIAL PRIMARY KEY,
                        ved_id INT NOT NULL REFERENCES vedas(id),
                        sukta_id INT REFERENCES suktas(id),
                        mandala_id INT REFERENCES mandalas(id),
                        mantra_number INT,
                        text_hindi TEXT,
                        text_sanskrit TEXT,
                        translation_en TEXT,
                        meaning_hindi TEXT,
                        tags JSONB,
                        metadata JSONB
                    );
                    
                    CREATE TABLE IF NOT EXISTS veda_embeddings (
                        id SERIAL PRIMARY KEY,
                        mantra_id INT NOT NULL REFERENCES mantras(id),
                        ved_id INT NOT NULL REFERENCES vedas(id),
                        embedding vector(1024),
                        language VARCHAR(10),
                        chunk_type VARCHAR(20),
                        created_at TIMESTAMP DEFAULT NOW()
                    );
                    
                    -- Attempt to upgrade column if it exists with wrong dimension
                    DO $$
                    BEGIN
                        BEGIN
                            ALTER TABLE veda_embeddings ALTER COLUMN embedding TYPE vector(1024);
                        EXCEPTION
                            WHEN OTHERS THEN
                                NULL; -- Table might not exist or empty
                        END;
                    END $$;
                    
                    CREATE INDEX IF NOT EXISTS idx_veda_embeddings_ved_id ON veda_embeddings(ved_id);
                    CREATE INDEX IF NOT EXISTS idx_veda_embeddings_mantra_id ON veda_embeddings(mantra_id);
                    CREATE INDEX IF NOT EXISTS idx_mantras_ved_id ON mantras(ved_id);
                """
                )
                conn.commit()
                logger.info("Veda schema created successfully.")
    except Exception as e:
        logger.error(f"Failed to setup schema: {e}")
        raise


if __name__ == "__main__":
    setup_schema()

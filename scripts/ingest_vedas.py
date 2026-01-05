import argparse
import logging
import sys
import os
import json
from typing import List, Dict


# Add project root to path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.ingestion.pdf_extractor import PdfExtractor
from src.ingestion.text_processor import TextProcessor
from src.ingestion.veda_parser import VedaParser
from src.db.db_manager import DatabaseManager
from src.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VedaIngestionPipeline:
    """Complete pipeline for Veda PDF → Database."""

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.extractor = PdfExtractor()
        self.processor = TextProcessor()
        self.parser = VedaParser()

    def ingest_ved_pdf(
        self, pdf_path: str, ved_name: str, ved_code: str, limit: int = None
    ):
        """Ingest single Veda PDF."""
        logger.info(f"Step 1: Ingesting {ved_name} from {pdf_path}...")

        if not os.path.exists(pdf_path):
            logger.error(f"File not found: {pdf_path}")
            return

        # Step 1: Extract PDF
        try:
            pages = self.extractor.extract_with_metadata(pdf_path, max_pages=limit)
            logger.info(f"  ✓ Extracted {len(pages)} pages")
        except Exception as e:
            logger.error(f"Extraction failed: {e}")
            return

        # Step 2: Clean text
        cleaned_pages = []
        for page in pages:
            page["text"] = self.processor.clean_text(page["text"])
            cleaned_pages.append(page)
        logger.info("  ✓ Cleaned text")

        # Step 3: Parse structure (Mandala → Sukta → Mantra)
        mantras = self.parser.parse_vedas(cleaned_pages, ved_code)
        logger.info(f"  ✓ Parsed {len(mantras)} mantras")

        if not mantras:
            logger.warning(
                "No mantras parsed. Checking if PDF content was extracted correctly."
            )
            # Fallback debug
            if len(cleaned_pages) > 0:
                logger.debug(f"First page sample: {cleaned_pages[0]['text'][:200]}")
            return

        # Step 4: Store in database
        self._store_mantras(mantras, ved_name, ved_code)
        logger.info(f"  ✓ Pipeline complete for {ved_name}")

    def _store_mantras(self, mantras: List[Dict], ved_name: str, ved_code: str):
        """Store parsed mantras in database."""
        try:
            with self.db._get_connection() as conn:
                with conn.cursor() as cursor:
                    # Insert Ved
                    cursor.execute(
                        """
                        INSERT INTO vedas (name, code, language, total_mantras) 
                        VALUES (%s, %s, %s, %s)
                        ON CONFLICT (id) DO NOTHING 
                        RETURNING id
                        """,
                        (ved_name, ved_code, "hi", len(mantras)),
                    )
                    # If conflict, we might need to select it.
                    # Since we don't have UNIQUE on name or code in schema (only id serial),
                    # let's assume we might need to query if RETURNING returns None (or handle duplicates by checking existence first)
                    # Actually schema says: CREATE TABLE vedas ... name VARCHAR(50). No unique constraint specified in setup script explicitly other than potentially implied in previous contexts,
                    # but let's be safe.

                    row = cursor.fetchone()
                    if row:
                        ved_id = row[0]
                    else:
                        # Check existence if not inserted (though simple INSERT without conflict clause on name would just duplicate,
                        # the setup script didn't add unique constraint on name.
                        # Let's clean up logic: Check if exists first)
                        cursor.execute(
                            "SELECT id FROM vedas WHERE name = %s", (ved_name,)
                        )
                        res = cursor.fetchone()
                        if res:
                            ved_id = res[0]
                        else:
                            # If we are here, something weird happened or we need to Force insert if previous one failed?
                            # Re-running insert might be simplest if no constraint.
                            # But better:
                            logger.info(
                                f"Veda {ved_name} already exists or didn't return ID directly."
                            )
                            cursor.execute(
                                "SELECT id FROM vedas WHERE name = %s", (ved_name,)
                            )
                            row_ex = cursor.fetchone()
                            if row_ex:
                                ved_id = row_ex[0]
                            else:
                                # Fallback insert if ON CONFLICT logic wasn't needed
                                cursor.execute(
                                    "INSERT INTO vedas (name, code, language, total_mantras) VALUES (%s, %s, %s, %s) RETURNING id",
                                    (ved_name, ved_code, "hi", len(mantras)),
                                )
                                ved_id = cursor.fetchone()[0]

                    # Note: Ideally we should handle Mandala/Sukta creation too to maintain FK constraints
                    # The current parser gives IDs but we need to create the parent records first.

                    # 4.1 Collect unique Mandalas and Suktas
                    unique_mandalas = set(
                        m["mandala_id"] for m in mantras if m["mandala_id"]
                    )
                    mandala_map = {}  # num -> db_id

                    for m_num in unique_mandalas:
                        if m_num == 0:
                            continue
                        cursor.execute(
                            "INSERT INTO mandalas (ved_id, mandala_number, name) VALUES (%s, %s, %s) RETURNING id",
                            (ved_id, m_num, f"Mandala {m_num}"),
                        )
                        mandala_map[m_num] = cursor.fetchone()[0]

                    # 4.2 Collect unique Suktas (keyed by mandala_id + sukta_num)
                    # The parser provides sukta number relative to... usually mandala.
                    unique_suktas = set(
                        (m["mandala_id"], m["sukta_id"])
                        for m in mantras
                        if m["sukta_id"]
                    )
                    sukta_map = {}  # (m_id, s_num) -> db_id

                    for m_num, s_num in unique_suktas:
                        if m_num == 0 or s_num == 0:
                            continue
                        m_db_id = mandala_map.get(m_num)
                        if not m_db_id:
                            continue

                        cursor.execute(
                            "INSERT INTO suktas (ved_id, mandala_id, sukta_number, name) VALUES (%s, %s, %s, %s) RETURNING id",
                            (ved_id, m_db_id, s_num, f"Sukta {s_num}"),
                        )
                        sukta_map[(m_num, s_num)] = cursor.fetchone()[0]

                    # 4.3 Insert Mantras
                    for mantra in mantras:
                        m_num = mantra.get("mandala_id")
                        s_num = mantra.get("sukta_id")

                        m_db_id = mandala_map.get(m_num)
                        s_db_id = sukta_map.get((m_num, s_num))

                        tag_json = json.dumps(mantra.get("tags", []))

                        cursor.execute(
                            """INSERT INTO mantras 
                               (ved_id, mandala_id, sukta_id, mantra_number, 
                                text_hindi, translation_en, tags)
                               VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                            (
                                ved_id,
                                m_db_id,
                                s_db_id,
                                mantra.get("mantra_number"),
                                mantra.get("text"),
                                mantra.get("translation"),
                                tag_json,
                            ),
                        )
                    conn.commit()
                    logger.info("Database commit successful.")

        except Exception as e:
            logger.error(f"Database error: {e}")
            raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", required=True, help="Path to Veda PDF")
    parser.add_argument(
        "--ved", required=True, help="Veda name (Rig Ved, Yajur Ved, etc.)"
    )
    parser.add_argument(
        "--code", required=True, help="Veda code (rig, yajur, sam, atharv)"
    )
    parser.add_argument("--limit", type=int, help="Limit number of pages to ingest")
    parser.add_argument(
        "--force", action="store_true", help="Force ingestion even if already processed"
    )
    args = parser.parse_args()

    from src.ingestion.utils import should_process, mark_processed

    if not should_process(args.pdf, args.force):
        logger.info(
            f"Skipping {args.ved} - already processed (use --force to override)."
        )
        sys.exit(0)

    db = DatabaseManager(settings.DATABASE_URL)
    pipeline = VedaIngestionPipeline(db)
    pipeline.ingest_ved_pdf(args.pdf, args.ved, args.code, args.limit)

    # Mark as processed
    mark_processed(args.pdf)

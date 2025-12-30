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
from src.ingestion.scripture_parsers import get_parser
from src.db.db_manager import DatabaseManager
from src.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ScriptureIngestionPipeline:
    """Generalized pipeline for Scripture PDF → Database."""

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.extractor = PdfExtractor()
        self.processor = TextProcessor()

    def ingest_pdf(
        self, pdf_path: str, name: str, code: str, scripture_type: str, limit: int = None
    ):
        """Ingest single scripture PDF."""
        logger.info(f"Step 1: Ingesting {name} ({scripture_type}) from {pdf_path}...")

        if not os.path.exists(pdf_path):
            logger.error(f"File not found: {pdf_path}")
            return

        # 1. Extract
        try:
            pages = self.extractor.extract_with_metadata(pdf_path, max_pages=limit)
            logger.info(f"  ✓ Extracted {len(pages)} pages")
        except Exception as e:
            logger.error(f"Extraction failed: {e}")
            return

        # 2. Clean
        cleaned_pages = []
        for page in pages:
            # Maybe skip generic header/footer removal for specific texts if needed?
            # For now, use standard processor.
            page["text"] = self.processor.clean_text(page["text"])
            cleaned_pages.append(page)
        logger.info("  ✓ Cleaned text")

        # 3. Parse
        parser = get_parser(scripture_type)
        # Note: 'code' passed to parse method mostly for tagging, 
        # but parser method signature is `parse(pages, code)` in Base/Veda parsers.
        # Check compatibility. BaseScriptureParser.parse matches VedaParser signature.
        verses = parser.parse(cleaned_pages, code)
        logger.info(f"  ✓ Parsed {len(verses)} verses")

        if not verses:
            logger.warning("No verses parsed. Check PDF content or parser patterns.")
            if len(cleaned_pages) > 0:
                logger.debug(f"Sample: {cleaned_pages[0]['text'][:200]}")
            return

        # 4. Store
        self._store_verses(verses, name, code)
        logger.info(f"  ✓ Pipeline complete for {name}")

    def _store_verses(self, verses: List[Dict], name: str, code: str):
        """Store parsed verses in database using Veda schema mapping."""
        try:
            with self.db._get_connection() as conn:
                with conn.cursor() as cursor:
                    # 4.1 Insert Scripture (as 'vedas' table entry)
                    cursor.execute(
                        "SELECT id FROM vedas WHERE name = %s", (name,)
                    )
                    res = cursor.fetchone()
                    if res:
                        scripture_id = res[0]
                    else:
                        cursor.execute(
                            """
                            INSERT INTO vedas (name, code, language, total_mantras) 
                            VALUES (%s, %s, %s, %s)
                            RETURNING id
                            """,
                            (name, code, "hi", len(verses)),
                        )
                        scripture_id = cursor.fetchone()[0]

                    # 4.2 Collect unique L1 (Mandalas)
                    # L1 = Kanda, Skanda, Adhyaya (for Gita)
                    unique_l1 = set(v["mandala_id"] for v in verses if v["mandala_id"])
                    l1_map = {} # num -> db_id

                    for num in unique_l1:
                        if num == 0: continue
                        cursor.execute(
                            "SELECT id FROM mandalas WHERE ved_id = %s AND mandala_number = %s",
                            (scripture_id, num)
                        )
                        res = cursor.fetchone()
                        if res:
                            l1_map[num] = res[0]
                        else:
                            cursor.execute(
                                "INSERT INTO mandalas (ved_id, mandala_number, name) VALUES (%s, %s, %s) RETURNING id",
                                (scripture_id, num, f"Section {num}")
                            )
                            l1_map[num] = cursor.fetchone()[0]

                    # 4.3 Collect unique L2 (Suktas)
                    # L2 = Sarga, Adhyaya (for Purana)
                    # For Gita, L2 is usually 0/None.
                    unique_l2 = set((v["mandala_id"], v["sukta_id"]) for v in verses if v["sukta_id"])
                    l2_map = {} # (l1, l2) -> db_id

                    for l1_num, l2_num in unique_l2:
                        if l1_num == 0 or l2_num == 0: continue
                        
                        l1_db_id = l1_map.get(l1_num)
                        if not l1_db_id: continue

                        cursor.execute(
                            "SELECT id FROM suktas WHERE ved_id = %s AND mandala_id = %s AND sukta_number = %s",
                            (scripture_id, l1_db_id, l2_num)
                        )
                        res = cursor.fetchone()
                        if res:
                            l2_map[(l1_num, l2_num)] = res[0]
                        else:
                            cursor.execute(
                                "INSERT INTO suktas (ved_id, mandala_id, sukta_number, name) VALUES (%s, %s, %s, %s) RETURNING id",
                                (scripture_id, l1_db_id, l2_num, f"Subsection {l2_num}")
                            )
                            l2_map[(l1_num, l2_num)] = cursor.fetchone()[0]

                    # 4.4 Insert Verses (Mantras)
                    for v in verses:
                        l1 = v.get("mandala_id")
                        l2 = v.get("sukta_id")
                        
                        l1_db = l1_map.get(l1)
                        l2_db = l2_map.get((l1, l2)) # Might be None if no L2
                        
                        tags = json.dumps(v.get("tags", []))
                        
                        cursor.execute(
                            """
                            INSERT INTO mantras 
                            (ved_id, mandala_id, sukta_id, mantra_number, text_hindi, translation_en, tags)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                            """,
                            (
                                scripture_id,
                                l1_db, # Can be None? Schema says REFERENCES mandalas(id). Usually nullable unless defined otherwise. 
                                       # Checked schema: "mandala_id INT REFERENCES mandalas(id)" -> Nullable default.
                                l2_db, # Can be None.
                                v.get("mantra_number"),
                                v.get("text"),
                                v.get("translation"),
                                tags
                            )
                        )
                    
                    conn.commit()
                    logger.info("Database commit successful.")

        except Exception as e:
            logger.error(f"Database error: {e}")
            raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", required=True, help="Path to PDF")
    parser.add_argument("--name", required=True, help="Scripture Name (e.g. Bhagavad Gita)")
    parser.add_argument("--code", required=True, help="Code (e.g. gita, ram)")
    parser.add_argument("--type", required=True, choices=["veda", "gita", "ramayana", "purana"], help="Scripture Type")
    parser.add_argument("--limit", type=int, help="Limit pages")
    parser.add_argument("--force", action="store_true", help="Force ingestion even if already processed")
    args = parser.parse_args()

    from src.ingestion.utils import should_process, mark_processed

    if not should_process(args.pdf, args.force):
        logger.info(f"Skipping {args.name} - already processed (use --force to override).")
        sys.exit(0)

    db = DatabaseManager(settings.DATABASE_URL)
    pipeline = ScriptureIngestionPipeline(db)
    pipeline.ingest_pdf(args.pdf, args.name, args.code, args.type, args.limit)
    
    # Mark as processed only if successful (implicitly, if no exception raised)
    mark_processed(args.pdf)

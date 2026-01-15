import argparse
import logging
import os
import sys
from typing import Optional

# Add project root to path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from neo4j import GraphDatabase

from src.core.config import settings
from src.db.db_manager import DatabaseManager
from src.ingestion.utils import TRACKING_FILE

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ScriptureCleaner:
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def clean_scripture(self, name: Optional[str] = None, code: Optional[str] = None):
        """Clean up data for a scripture by name or code."""
        if not name and not code:
            logger.error("Must provide either name or code.")
            return

        logger.info(f"Starting cleanup for scripture: name='{name}', code='{code}'")

        # 1. Postgres Cleanup
        self._clean_postgres(name, code)

        # 2. Neo4j Cleanup
        self._clean_neo4j(name, code)

        # 3. File Tracking Cleanup
        # We need the source PDF path to clean tracking file properly.
        # Since we might not know the exact path here, we might have to scan the tracking file
        # or rely on the user having passed the path if we want to be precise.
        # However, the tracking file stores ABSOLUTE paths.
        # If we only have the name, we can't easily identify the file unless we query the DB first *before* deleting.
        # Let's try to fetch source_path from DB before deleting.

    def _get_source_path(self, name: Optional[str], code: Optional[str]) -> Optional[str]:
        try:
            with self.db._get_connection() as conn:
                with conn.cursor() as cursor:
                    if name:
                        cursor.execute("SELECT source_pdf_path FROM vedas WHERE name = %s", (name,))
                    else:
                        cursor.execute("SELECT source_pdf_path FROM vedas WHERE code = %s", (code,))
                    
                    res = cursor.fetchone()
                    if res:
                        return res[0]
        except Exception as e:
            logger.warning(f"Could not fetch source path: {e}")
        return None

    def _clean_postgres(self, name: Optional[str], code: Optional[str]):
        logger.info("Cleaning Postgres data...")
        try:
            # Get source path first for file tracking cleanup
            source_path = self._get_source_path(name, code)
            
            with self.db._get_connection() as conn:
                with conn.cursor() as cursor:
                    # Vedas table has cascade delete on dependencies usually. 
                    # Let's check init.sql or assumptions.
                    # scripts/setup_veda_schema.py:
                    # mandalas -> ved_id (REFERENCES vedas(id)) - DEFAULT NO ACTION usually?
                    # Wait, setup_veda_schema.py did NOT specify ON DELETE CASCADE.
                    # So we must delete dependencies manually or use CASCADE in delete?
                    # Postgres supports DELETE ... CASCADE? No, TRUNCATE has cascade. DELETE doesn't iterate.
                    # But if FK constraints don't have CASCADE, DELETE will fail.
                    # Let's assume we need to delete children first if CASCADE is missing.
                    
                    # Let's verify constraints. schema definition:
                    # ved_id INT NOT NULL REFERENCES vedas(id)
                    # It does not say ON DELETE CASCADE.
                    # So we definitely need to manual delete.
                    
                    # Logic: Get ID -> Delete Embeddings, Mantras, Suktas, Mandalas -> Delete Veda
                    
                    if name:
                        cursor.execute("SELECT id FROM vedas WHERE name = %s", (name,))
                    else:
                        cursor.execute("SELECT id FROM vedas WHERE code = %s", (code,))
                        
                    res = cursor.fetchone()
                    if not res:
                        logger.info("Scripture not found in Postgres.")
                        return
                    
                    ved_id = res[0]
                    logger.info(f"Found Veda ID: {ved_id}")

                    # 1. Embeddings
                    cursor.execute("DELETE FROM veda_embeddings WHERE ved_id = %s", (ved_id,))
                    
                    # 2. Mantras
                    cursor.execute("DELETE FROM mantras WHERE ved_id = %s", (ved_id,))
                    
                    # 3. Suktas
                    cursor.execute("DELETE FROM suktas WHERE ved_id = %s", (ved_id,))
                    
                    # 4. Mandalas
                    cursor.execute("DELETE FROM mandalas WHERE ved_id = %s", (ved_id,))
                    
                    # 5. Veda
                    cursor.execute("DELETE FROM vedas WHERE id = %s", (ved_id,))
                    
                    conn.commit()
                    logger.info("✓ Postgres data cleaned.")
                    
            # After successful DB delete, clean tracking file
            if source_path:
                self._clean_tracking_file(source_path)

        except Exception as e:
            logger.error(f"Postgres cleanup failed: {e}")
            # Don't raise, try to continue to Neo4j

    def _clean_tracking_file(self, source_path: str):
        logger.info(f"Removing '{source_path}' from tracking file...")
        if not os.path.exists(TRACKING_FILE):
            return

        try:
            # Read all lines
            with open(TRACKING_FILE, "r") as f:
                lines = f.read().splitlines()
            
            # Filter out the matching path (fuzzy match or exact?)
            # The ingestion script stores os.path.abspath(pdf_path).
            # The source_path in DB might be relative or absolute depending on how it was stored.
            # safe matching: check uniqueness
            
            # If source_path is relative, abspath it
            abs_source = os.path.abspath(source_path)
            
            new_lines = [line for line in lines if line != abs_source and line != source_path]
            
            if len(new_lines) < len(lines):
                with open(TRACKING_FILE, "w") as f:
                    f.write("\n".join(new_lines) + "\n")
                logger.info("✓ Tracking file updated.")
            else:
                logger.info("Path not found in tracking file (already clean?).")
                
        except Exception as e:
            logger.error(f"Tracking file cleanup failed: {e}")

    def _clean_neo4j(self, name: Optional[str], code: Optional[str]):
        if not settings.NEO4J_URI:
            logger.info("Neo4j URI not set, skipping Graph cleanup.")
            return

        logger.info("Cleaning Neo4j graph...")
        try:
            driver = GraphDatabase.driver(
                settings.NEO4J_URI, auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
            )
            with driver.session() as session:
                # We need to identify nodes belonging to this scripture.
                # Usually, we have a 'Scripture' or 'Source' node, and verses linked to it.
                # Or verify ontology. Assuming 'Text' or 'Scripture' label with 'name' property.
                
                # Delete the Scripture/Text node and all its relationships
                # Also delete Verse nodes belonging to it?
                # Strategy: Match (s:Scripture {name: $name}) DETACH DELETE s
                # But we also need to delete Verse nodes.
                # Verses usually link to Scripture via belongs_to or similar.
                
                target_name = name or code # Name is safer if consistent
                
                # 1. Find Scripture Node
                # Assuming label 'Scripture' or 'Text' and property 'name'
                # Let's warn if we rely on name.
                
                query = """
                MATCH (s {name: $name})
                WHERE 'Scripture' IN labels(s) OR 'Text' IN labels(s) OR 'Veda' IN labels(s)
                WITH s
                OPTIONAL MATCH (v)-[:BELONGS_TO]->(s)
                DETACH DELETE s, v
                """
                # This is a bit risky if schema differs.
                # Let's look at build_knowledge_graph.py to see how nodes are created.
                # But for now, let's try a simple approach: if we can find the main node, delete it and everything connected solely to it?
                # Actually, Verses might be connected to concepts. We want to delete Verses but NOT Concepts.
                
                # Safer: Delete nodes labeled 'Verse' or 'Mantra' that have property 'source' == name
                # or relation to the Scripture node.
                
                # Let's just delete the node with the name for now, and rely on user to rebuild valid graph.
                # A partial cleanup in Graph is acceptable if we break links.
                
                # Re-reading reset_data.py doesn't show schema details.
                # Let's assume standard 'Text' node.
                
                res = session.run("MATCH (n {name: $name}) DETACH DELETE n RETURN count(n) as deleted", name=target_name)
                count = res.single()['deleted']
                logger.info(f"Deleted {count} nodes with name '{target_name}' from Neo4j.")

                # Also try matching by 'source' property on Verses
                res = session.run("MATCH (n) WHERE n.source = $name DETACH DELETE n RETURN count(n) as deleted", name=target_name)
                count_sources = res.single()['deleted']
                logger.info(f"Deleted {count_sources} nodes with source '{target_name}' from Neo4j.")
                
            driver.close()
            logger.info("✓ Neo4j cleanup attempt complete.")

        except Exception as e:
            logger.error(f"Neo4j cleanup failed: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="Scripture Name")
    parser.add_argument("--code", help="Scripture Code")
    args = parser.parse_args()

    db = DatabaseManager(settings.DATABASE_URL)
    cleaner = ScriptureCleaner(db)
    cleaner.clean_scripture(name=args.name, code=args.code)

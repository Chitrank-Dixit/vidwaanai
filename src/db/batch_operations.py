from typing import List, Dict, Any
from src.db.db_manager import DatabaseManager
from src.core.logger import get_logger
import psycopg2.extras

logger = get_logger(__name__)

class BatchOperations:
    """Helper for batch database operations."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def batch_insert_verses(self, verses: List[Dict[str, Any]]) -> int:
        """Batch insert verses."""
        if not verses:
            return 0
            
        try:
            with self.db._get_connection() as conn:
                with conn.cursor() as cursor:
                    query = """
                        INSERT INTO verses (scripture_id, chapter_number, verse_number, verse_text, translation_en, themes, speakers)
                        VALUES %s
                        ON CONFLICT (scripture_id, chapter_number, verse_number) DO NOTHING
                    """
                    
                    values = [
                        (
                            v['scripture_id'],
                            v['chapter_number'],
                            v['verse_number'],
                            v['verse_text'],
                            v.get('translation_en', ''),
                            v.get('themes', []),
                            v.get('speakers', [])
                        )
                        for v in verses
                    ]
                    
                    psycopg2.extras.execute_values(cursor, query, values)
                    conn.commit()
                    return len(values)
        except Exception as e:
            logger.error(f"Batch insert verses failed: {e}")
            raise

    def batch_insert_embeddings(self, embeddings_data: List[Dict[str, Any]]) -> int:
        """Batch insert embeddings."""
        if not embeddings_data:
            return 0
            
        try:
            with self.db._get_connection() as conn:
                with conn.cursor() as cursor:
                    query = """
                        INSERT INTO scripture_embeddings (verse_id, embedding, language, chunk_index, processed)
                        VALUES %s
                        ON CONFLICT (verse_id, language, chunk_index) 
                        DO UPDATE SET embedding = EXCLUDED.embedding, processed = EXCLUDED.processed
                    """
                    
                    values = []
                    for item in embeddings_data:
                        # Format embedding as string for pgvector
                        emb_str = "[" + ",".join(str(e) for e in item['embedding']) + "]"
                        values.append((
                            item['verse_id'],
                            emb_str,
                            item.get('language', 'en'),
                            item.get('chunk_index', 0),
                            item.get('processed', True)
                        ))
                    
                    psycopg2.extras.execute_values(cursor, query, values)
                    conn.commit()
                    return len(values)
        except Exception as e:
            logger.error(f"Batch insert embeddings failed: {e}")
            raise

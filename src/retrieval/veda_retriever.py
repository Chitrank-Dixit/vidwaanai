from typing import List, Dict, Optional, Any
import logging
from src.db.db_manager import DatabaseManager
from src.embeddings.veda_embedder import VedaEmbedder

logger = logging.getLogger(__name__)


class VedaRetriever:
    """Retrieve Veda mantras using semantic search."""

    def __init__(
        self, db_manager: DatabaseManager, embedder: Optional[VedaEmbedder] = None
    ):
        self.db = db_manager
        self.embedder = embedder or VedaEmbedder()

    def search(
        self, query: str, language: str = "hi", top_k: int = 5, threshold: float = 0.5
    ) -> List[Dict[str, Any]]:
        """
        Search for mantras similar to query.
        """
        # Embed query
        query_embedding = self.embedder.embed_text(query, is_query=True)
        embedding_str = "[" + ",".join(str(e) for e in query_embedding) + "]"

        results = []
        try:
            with self.db._get_connection() as conn:
                with conn.cursor() as cursor:
                    # Query using cosine similarity (<=> operator in pgvector)
                    # Note: <=> is cosine distance, so 1 - distance = similarity (roughly)
                    # Actually <=> is cosine distance. 0 = identical.
                    # So we want ORDER BY distance ASC.

                    sql = """
                        SELECT 
                            m.id, 
                            m.text_hindi, 
                            m.translation_en, 
                            m.mantra_number,
                            v.name as ved_name,
                            md.name as mandala_name,
                            s.name as sukta_name,
                            (ve.embedding <=> %s::vector) as distance
                        FROM veda_embeddings ve
                        JOIN mantras m ON ve.mantra_id = m.id
                        JOIN vedas v ON m.ved_id = v.id
                        LEFT JOIN mandalas md ON m.mandala_id = md.id
                        LEFT JOIN suktas s ON m.sukta_id = s.id
                        WHERE ve.chunk_type = 'mantra'
                        ORDER BY distance ASC
                        LIMIT %s
                    """

                    cursor.execute(sql, (embedding_str, top_k))
                    rows = cursor.fetchall()

                    for row in rows:
                        # row: id, text, trans, mantra_num, ved_name, mandala, sukta, distance
                        # Filter by threshold if needed (distance < 0.5 means sim > 0.5 approx)
                        if row[7] > (1 - threshold):
                            # If threshold is similarity 0.5, we want distance < 0.5?
                            # Usually cosine distance is 0..2.
                            # Let's map it: sim = 1 - distance.
                            pass

                        results.append(
                            {
                                "id": row[0],
                                "text": row[1],
                                "translation": row[2],
                                "source": f"{row[4]} {row[5]} {row[6]}",
                                "mantra_num": row[3],
                                "score": 1 - float(row[7]),  # Similarity
                                "distance": float(row[7]),
                            }
                        )

        except Exception as e:
            logger.error(f"Search failed: {e}")

        return results

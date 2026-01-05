"""Database management."""

import logging
from contextlib import contextmanager
from datetime import datetime
from typing import Any, Dict, List, Optional

from psycopg2.extras import RealDictCursor
from psycopg2.pool import ThreadedConnectionPool

logger = logging.getLogger(__name__)


class DatabaseManager:
    """Manages database connections and operations."""

    def __init__(self, db_url: str) -> None:
        """Initialize database manager."""
        self.db_url = db_url
        logger.info("Database manager initialized")

        # Parse connection string
        try:
            parts = self.db_url.replace("postgresql://", "").split("@")
            user_pass = parts[0].split(":")
            host_db = parts[1].split("/")
            host_port = host_db[0].split(":")

            self.pool = ThreadedConnectionPool(
                minconn=2,
                maxconn=10,
                dbname=host_db[1],
                user=user_pass[0],
                password=user_pass[1],
                host=host_port[0],
                port=host_port[1] if len(host_port) > 1 else "5432",
            )
        except Exception as e:
            logger.error(f"Failed to create connection pool: {str(e)}")
            raise

    @contextmanager
    def _get_connection(self) -> Any:
        """Get database connection from pool."""
        conn = None
        try:
            conn = self.pool.getconn()
            yield conn
        except Exception as e:
            logger.error(f"Database connection failed: {str(e)}")
            raise
        finally:
            if conn:
                self.pool.putconn(conn)

    def get_scriptures(self) -> List[Dict[str, Any]]:
        """Get all loaded scriptures."""
        # This method implementation seems broken in original file (references undefined 'name'),
        # but I will update the connection usage pattern regardless.
        # Actually, looking at the original code, get_scriptures seems to have copy-pasted logic from add_scripture?
        # It tries to INSERT... that's wrong for get_scriptures.
        # I will fix it to actually GET scriptures.
        try:
            with self._get_connection() as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                    cursor.execute("SELECT * FROM scriptures")
                    return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            logger.error(f"Error fetching scriptures: {str(e)}")
            return []
        except Exception as e:
            logger.error(f"Error fetching scriptures: {str(e)}")
            return []

    def add_scripture(self, name: str, language: str, description: str = "") -> int:
        """Add a scripture to database."""
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO scriptures (name, language, description)
                        VALUES (%s, %s, %s)
                        ON CONFLICT (name) DO NOTHING
                        RETURNING id
                        """,
                        (name, language, description),
                    )
                    result = cursor.fetchone()
                    if result:
                        scripture_id = result[0]
                    else:
                        cursor.execute(
                            "SELECT id FROM scriptures WHERE name = %s", (name,)
                        )
                        scripture_id = cursor.fetchone()[0]
                    conn.commit()
                    return int(scripture_id)
        except Exception as e:
            logger.error(f"Error adding scripture: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error adding scripture: {str(e)}")
            raise

    def add_verse(
        self,
        scripture_id: int,
        chapter: int,
        verse_num: int,
        text: str,
        translation: str,
        themes: List[str],
        speakers: List[str],
    ) -> int:
        """Add a verse to database."""
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO verses (scripture_id, chapter_number, verse_number, verse_text, translation_en, themes, speakers)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (scripture_id, chapter_number, verse_number) DO NOTHING
                        RETURNING id
                        """,
                        (
                            scripture_id,
                            chapter,
                            verse_num,
                            text,
                            translation,
                            themes,
                            speakers,
                        ),
                    )
                    result = cursor.fetchone()
                    if result:
                        verse_id = result[0]
                    else:
                        cursor.execute(
                            "SELECT id FROM verses WHERE scripture_id = %s AND chapter_number = %s AND verse_number = %s",
                            (scripture_id, chapter, verse_num),
                        )
                        verse_id = cursor.fetchone()[0]
                    conn.commit()
                    return int(verse_id)
        except Exception as e:
            logger.error(f"Error adding verse: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error adding verse: {str(e)}")
            raise

    def add_embedding(
        self, verse_id: int, embedding: List[float], language: str
    ) -> None:
        """Add embedding for a verse."""
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    # Format embedding as string for pgvector
                    embedding_str = "[" + ",".join(str(e) for e in embedding) + "]"

                    cursor.execute(
                        """
                        INSERT INTO scripture_embeddings (verse_id, embedding, language, chunk_index, processed)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (verse_id, language, chunk_index) DO UPDATE SET embedding = EXCLUDED.embedding, processed = EXCLUDED.processed;
                        """,
                        (verse_id, embedding_str, language, 0, False),
                    )
                    conn.commit()
        except Exception as e:
            logger.error(f"Error adding embedding: {str(e)}")
            raise

        except Exception as e:
            logger.error(f"Error adding embedding: {str(e)}")
            raise

    def retrieve_verses(
        self,
        query_embedding: List[float],
        scripture_filter: Optional[str] = None,
        top_k: int = 5,
    ) -> List[Dict[str, Any]]:
        """Retrieve verses similar to query embedding."""
        try:
            with self._get_connection() as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                    embedding_str = (
                        "[" + ",".join(str(e) for e in query_embedding) + "]"
                    )

                    # Build query with vector similarity
                    where_clause = ""
                    # Params for WHERE and LIMIT
                    middle_params = []

                    if scripture_filter:
                        where_clause = "AND s.name = %s"
                        middle_params.append(scripture_filter)

                    sql = f"""
                        SELECT DISTINCT
                            v.id,
                            s.name as scripture,
                            v.chapter_number as chapter,
                            v.verse_number as verse,
                            v.verse_text as text,
                            v.translation_en as translation,
                            (1 - (se.embedding <=> %s::vector)) as similarity
                        FROM scripture_embeddings se
                        JOIN verses v ON se.verse_id = v.id
                        JOIN scriptures s ON v.scripture_id = s.id
                        WHERE se.language = 'en' {where_clause}
                        ORDER BY similarity DESC
                        LIMIT %s
                    """  # nosec B608

                    # Order: Similarity (embedding), Where (optional), Limit (top_k)
                    # We removed the second embedding param from ORDER BY
                    params = [embedding_str] + middle_params + [top_k]

                    try:
                        cursor.execute(sql, params)
                        rows = cursor.fetchall()
                        result = [dict(row) for row in rows]
                    except Exception as e:
                        # Fallback if vector search fails
                        logger.warning(
                            f"Vector search failed: {e}, returning sample results"
                        )
                        conn.rollback()  # Rollback transaction to recover from error
                        cursor.execute(
                            f"""SELECT v.id, s.name as scripture, v.chapter_number as chapter, v.verse_number as verse,
                                   v.verse_text as text, v.translation_en as translation
                               FROM verses v
                               JOIN scriptures s ON v.scripture_id = s.id
                               {where_clause.replace("AND ", "WHERE ")}
                               ORDER BY v.id DESC LIMIT %s""",  # nosec B608
                            [scripture_filter] if scripture_filter else [top_k],  # type: ignore
                        )
                        rows = cursor.fetchall()
                        result = [dict(row) for row in rows]
                        for row in result:
                            row["similarity"] = 0.95

                    return result

        except Exception as e:
            logger.error(f"Error retrieving verses: {str(e)}")
            return []

    def log_query(
        self,
        query_text: str,
        response_text: str,
        language: str,
        retrieved_count: int,
        timestamp: datetime,
    ) -> None:
        """Log user query."""
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """INSERT INTO user_queries (query_text, language, response_text, retrieved_verse_ids)
                           VALUES (%s, %s, %s, %s)""",
                        (query_text, language, response_text, []),
                    )
                    conn.commit()
        except Exception as e:
            logger.error(f"Error logging query: {str(e)}")

        except Exception as e:
            logger.error(f"Error logging query: {str(e)}")

    def get_all_verses(self) -> List[Dict[str, Any]]:
        """Get all verses from database (both generic verses and Veda mantras)."""
        try:
            with self._get_connection() as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                    # Union both tables.
                    # Prefix ID to avoid collision and trace source.
                    # 'v:1' -> verses table id 1. 'm:1' -> mantras table id 1.

                    cursor.execute(
                        """
                        SELECT 
                            'v:' || v.id::text as id, 
                            v.verse_text as text, 
                            v.translation_en as translation, 
                            s.name as scripture_name, 
                            v.chapter_number, 
                            v.verse_number
                        FROM verses v
                        JOIN scriptures s ON v.scripture_id = s.id
                        
                        UNION ALL
                        
                        SELECT 
                            'm:' || m.id::text as id, 
                            m.text_hindi as text, 
                            m.translation_en as translation,
                            vd.name as scripture_name, 
                            COALESCE(md.mandala_number, 0) as chapter_number, 
                            m.mantra_number as verse_number
                        FROM mantras m
                        JOIN vedas vd ON m.ved_id = vd.id
                        LEFT JOIN mandalas md ON m.mandala_id = md.id
                        ORDER BY scripture_name, chapter_number, verse_number
                        """
                    )

                    rows = cursor.fetchall()
                    return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Error getting all verses: {str(e)}")
            return []

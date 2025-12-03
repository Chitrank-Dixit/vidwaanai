import os
import sys
import psycopg2
from dotenv import load_dotenv

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv()

from src.core.logger import get_logger

logger = get_logger(__name__)


def explain_query(query_text: str, params: tuple = None):
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        logger.error("DATABASE_URL not set")
        return

    try:
        conn = psycopg2.connect(db_url)
        cursor = conn.cursor()

        print(f"\n--- Explaining Query ---\n{query_text}\n")

        # Use EXPLAIN (ANALYZE, BUFFERS) for detailed stats
        # Note: This actually executes the query!
        cursor.execute(f"EXPLAIN (ANALYZE, BUFFERS) {query_text}", params)

        plan = cursor.fetchall()
        for row in plan:
            print(row[0])

    except Exception as e:
        logger.error(f"Explain failed: {e}")
    finally:
        if "conn" in locals() and conn:
            conn.close()


if __name__ == "__main__":
    # Example usage with a common retrieval query
    sample_query = """
        SELECT v.id, v.verse_text 
        FROM verses v 
        JOIN scriptures s ON v.scripture_id = s.id 
        WHERE s.name = 'Bhagavad Gita' 
        LIMIT 5
    """
    explain_query(sample_query)

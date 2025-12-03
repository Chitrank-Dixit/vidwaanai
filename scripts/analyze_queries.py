import os
import sys
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
from tabulate import tabulate

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv()

from src.core.logger import get_logger

logger = get_logger(__name__)


def analyze_queries():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        logger.error("DATABASE_URL not set")
        return

    try:
        conn = psycopg2.connect(db_url)
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        # Check if pg_stat_statements is enabled
        try:
            cursor.execute("SELECT * FROM pg_stat_statements LIMIT 1")
        except psycopg2.errors.UndefinedTable:
            logger.warning(
                "pg_stat_statements extension not enabled or not accessible."
            )
            logger.info(
                "To enable: CREATE EXTENSION pg_stat_statements; in your database."
            )
            logger.info(
                "Note: It must also be added to shared_preload_libraries in postgresql.conf"
            )
            return

        print("\n--- Top 10 Slowest Queries ---")
        cursor.execute(
            """
            SELECT 
                substring(query, 1, 50) as query_snippet,
                calls,
                total_exec_time / 1000 as total_time_sec,
                mean_exec_time as avg_time_ms,
                rows
            FROM pg_stat_statements
            ORDER BY mean_exec_time DESC
            LIMIT 10
        """
        )

        rows = cursor.fetchall()
        if rows:
            print(tabulate(rows, headers="keys", tablefmt="pretty"))
        else:
            print("No query stats available.")

        print("\n--- Top 10 Most Frequent Queries ---")
        cursor.execute(
            """
            SELECT 
                substring(query, 1, 50) as query_snippet,
                calls,
                total_exec_time / 1000 as total_time_sec,
                mean_exec_time as avg_time_ms
            FROM pg_stat_statements
            ORDER BY calls DESC
            LIMIT 10
        """
        )

        rows = cursor.fetchall()
        if rows:
            print(tabulate(rows, headers="keys", tablefmt="pretty"))

    except Exception as e:
        logger.error(f"Analysis failed: {e}")
    finally:
        if "conn" in locals() and conn:
            conn.close()


if __name__ == "__main__":
    analyze_queries()

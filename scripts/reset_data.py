import os
import sys
import psycopg2
from dotenv import load_dotenv
from neo4j import GraphDatabase

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.core.config import settings

load_dotenv()


def reset_data():
    db_url = os.getenv("DATABASE_URL", "")
    if not db_url:
        print("No DATABASE_URL set.")
        return

    try:
        conn = psycopg2.connect(db_url)
        cursor = conn.cursor()

        print("Truncating tables...")
        # Order matters due to FKs
        cursor.execute(
            "TRUNCATE TABLE scripture_embeddings, verses, scriptures, user_queries, veda_embeddings, mantras, suktas, mandalas, vedas RESTART IDENTITY CASCADE;"
        )
        conn.commit()
        print("✓ Tables truncated successfully.")

        cursor.close()
        conn.close()

        # Clear Neo4j
        print("Clearing Neo4j graph...")
        driver = GraphDatabase.driver(
            settings.NEO4J_URI, auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
        )
        with driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
            # Also drop constraints if needed? For a full fresh start, yes.
            session.run("CALL apoc.schema.assert({},{},true)")
        driver.close()
        print("✓ Neo4j graph cleared successfully.")

    except Exception as e:
        print(f"Error resetting data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    reset_data()

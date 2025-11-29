# scripts/wait-for-postgres.py
import os
import time
import psycopg2
from psycopg2 import OperationalError


def wait_for_db():
    """Waits for the PostgreSQL database to be ready."""
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        print("DATABASE_URL environment variable not set. Exiting.")
        exit(1)

    retries = 10
    wait_seconds = 5
    for i in range(retries):
        try:
            conn = psycopg2.connect(db_url)
            conn.close()
            print("✓ Database is ready!")
            return
        except OperationalError as e:
            print(f"Database not ready yet... ({e}). Retrying in {wait_seconds}s.")
            time.sleep(wait_seconds)

    print("✗ Database did not become available after multiple retries. Exiting.")
    exit(1)


if __name__ == "__main__":
    wait_for_db()

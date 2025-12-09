import os
import sys
import psycopg2
from dotenv import load_dotenv

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

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
            "TRUNCATE TABLE scripture_embeddings, verses, scriptures, user_queries RESTART IDENTITY CASCADE;"
        )
        conn.commit()
        print("✓ Tables truncated successfully.")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error resetting data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    reset_data()

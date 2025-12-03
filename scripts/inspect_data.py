import os
import sys
from dotenv import load_dotenv

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv()

from src.db.db_manager import DatabaseManager  # noqa: E402


def inspect_data():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        print("DATABASE_URL not set")
        return

    db_manager = DatabaseManager(db_url)

    with db_manager._get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT v.id, s.name, v.chapter_number, v.verse_number, v.translation_en 
                FROM verses v 
                JOIN scriptures s ON v.scripture_id = s.id
                LIMIT 50;
            """
            )
            rows = cursor.fetchall()

            print(f"Found {len(rows)} verses:")
            for row in rows:
                print(f"ID: {row[0]} | {row[1]} {row[2]}.{row[3]} | {row[4][:100]}...")


if __name__ == "__main__":
    inspect_data()

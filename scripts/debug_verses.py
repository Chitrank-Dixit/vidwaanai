import os
import sys

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.db.db_manager import DatabaseManager
from dotenv import load_dotenv

load_dotenv()


def debug_verses():
    db_manager = DatabaseManager(os.getenv("DATABASE_URL", ""))
    verses = db_manager.get_all_verses()

    print(f"Total verses found: {len(verses)}")
    print("Sample Signatures:")
    for v in verses[:5]:
        sig = f"{v['scripture_name']} {v['chapter_number']}:{v['verse_number']}"
        print(f" - '{sig}'")


if __name__ == "__main__":
    debug_verses()

#!/usr/bin/env python3
"""Load sample scripture data into database."""

import os
import sys
from dotenv import load_dotenv
from typing import Any, Dict

load_dotenv()

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

from src.db.db_manager import DatabaseManager  # noqa: E402
from src.rag.embeddings import EmbeddingManager  # noqa: E402


def load_sample_data() -> None:
    """Load sample scriptures."""
    try:
        db_manager = DatabaseManager(os.getenv("DATABASE_URL", ""))
        embeddings = EmbeddingManager()

        # Sample verses for demonstration
        sample_data: Dict[str, Any] = {
            "Bhagavad Gita": {
                "language": "sanskrit",
                "verses": [
                    {
                        "chapter": 2,
                        "verse": 47,
                        "text": "karmany evadhikaras te ma phalesu kadacana",
                        "translation": "You have a right to perform your prescribed duty, but you are not entitled to the fruits of action.",
                        "themes": ["karma", "duty"],
                        "speakers": ["Krishna"],
                    },
                    {
                        "chapter": 2,
                        "verse": 46,
                        "text": "yavat artha udapane sarvatah samplutodake",
                        "translation": "As long as there are necessities of life to be derived from agricultural and other occupations, there is no need for any other occupation.",
                        "themes": ["karma yoga", "duty"],
                        "speakers": ["Krishna"],
                    },
                ],
            },
            "Ramayana": {
                "language": "sanskrit",
                "verses": [
                    {
                        "chapter": 1,
                        "verse": 1,
                        "text": "tapasya swa-niyamair yuktah",
                        "translation": "Lord Rama performed tapasya (austerity) with self-discipline.",
                        "themes": ["dharma", "virtue"],
                        "speakers": ["Narrator"],
                    }
                ],
            },
            "Mahabharata": {
                "language": "sanskrit",
                "verses": [
                    {
                        "chapter": 1,
                        "verse": 1,
                        "text": "nara-narayana-sahitam",
                        "translation": "The great war of the Mahabharata with Nara and Narayana.",
                        "themes": ["dharma", "war"],
                        "speakers": ["Vyasa"],
                    }
                ],
            },
        }

        print("Loading sample data...")

        for scripture_name, data in sample_data.items():
            print(f"\nLoading {scripture_name}...")

            # Add scripture
            scripture_id = db_manager.add_scripture(
                name=scripture_name,
                language=data["language"],
                description=f"{scripture_name} - Sample Data",
            )

            # Add verses and embeddings
            for verse_data in data["verses"]:
                verse_id = db_manager.add_verse(
                    scripture_id=scripture_id,
                    chapter=verse_data["chapter"],
                    verse_num=verse_data["verse"],
                    text=verse_data["text"],
                    translation=verse_data["translation"],
                    themes=verse_data["themes"],
                    speakers=verse_data["speakers"],
                )

                # Generate and store embeddings
                embedding_en = embeddings.embed_text(verse_data["translation"])
                if isinstance(embedding_en[0], list):
                    embedding_en = embedding_en[0]
                embedding_sa = embeddings.embed_text(verse_data["text"])
                if isinstance(embedding_sa[0], list):
                    embedding_sa = embedding_sa[0]

                db_manager.add_embedding(
                    verse_id=verse_id, embedding=embedding_en, language="en"  # type: ignore
                )
                db_manager.add_embedding(
                    verse_id=verse_id, embedding=embedding_sa, language="sa"  # type: ignore
                )

            print(f"✓ {scripture_name}: {len(data['verses'])} verses loaded")

        print("\n✓ Sample data loaded successfully!")

    except Exception as e:
        print(f"ERROR: {str(e)}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    load_sample_data()

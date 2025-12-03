import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.language.language_detector import LanguageDetector
from src.rag.multilingual_search import MultilingualSearch


def test_language(name: str, code: str, sample_text: str) -> None:
    print(f"\n--- Testing {name} ({code}) ---")

    # Test detection
    detector = LanguageDetector()
    d_code, d_name, d_conf = detector.detect_language(sample_text)
    print(f"Detection: {d_name} ({d_code}) - Confidence: {d_conf:.2f}")

    if d_code != code:
        print(f"❌ Detection Mismatch! Expected {code}, got {d_code}")
    else:
        print("✅ Detection Correct")

    # Test processing
    search = MultilingualSearch()
    result = search.process_query(sample_text)

    print(f"Processed Text: {result['processed_text']}")
    print(f"Embedding Shape: {len(result['embedding'])}")
    print("✅ Processing Successful")


if __name__ == "__main__":
    # Malayalam
    test_language("Malayalam", "ml", "നിങ്ങളുടെ പേര് എന്താണ്")  # "What is your name?"

    # Bengali
    test_language("Bengali", "bn", "আপনার নাম কি")  # "What is your name?"

    # Marathi
    test_language("Marathi", "mr", "तुझे नाव काय आहे")  # "What is your name?"

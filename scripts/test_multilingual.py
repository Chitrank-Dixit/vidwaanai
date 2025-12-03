import os
import sys
from dotenv import load_dotenv

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv()

from src.language.language_detector import LanguageDetector
from src.language.hindi_processor import HindiProcessor
from src.rag.multilingual_search import MultilingualSearch


def test_language_detection():
    print("\n--- Testing Language Detection ---")
    detector = LanguageDetector()

    test_cases = [
        ("This is an English sentence.", "en"),
        ("यह एक हिंदी वाक्य है।", "hi"),
        ("આ એક ગુજરાતી વાક્ય છે.", "gu"),
        ("இது ஒரு தமிழ் வாக்கியம்.", "ta"),
        ("ఇది తెలుగు వాక్యం.", "te"),
        ("ಇದು ಕನ್ನಡ ವಾಕ್ಯ.", "kn"),
    ]

    for text, expected in test_cases:
        code, name, conf = detector.detect_language(text)
        script = detector.detect_script(text)
        print(f"Text: {text}")
        print(f"Detected: {name} ({code}), Script: {script}, Confidence: {conf:.2f}")
        if code == expected:
            print("✅ PASS")
        else:
            print(f"❌ FAIL (Expected {expected})")


def test_hindi_processing():
    print("\n--- Testing Hindi Processing ---")
    processor = HindiProcessor()

    text = "धर्म क्या है? और कृष्ण की भूमिका क्या है?"
    print(f"Original: {text}")

    processed = processor.preprocess_hindi(text)
    print(f"Normalized: {processed['normalized']}")
    print(f"Tokens: {processed['tokens']}")
    print(f"Filtered (No Stopwords): {processed['filtered_tokens']}")

    # Check stopword removal
    if (
        "है" not in processed["filtered_tokens"]
        and "और" not in processed["filtered_tokens"]
    ):
        print("✅ Stopwords removed correctly")
    else:
        print("❌ Stopword removal failed")


def test_multilingual_search_flow():
    print("\n--- Testing Multilingual Search Flow ---")
    ms = MultilingualSearch()

    query = "धर्म क्या है?"
    print(f"Processing Query: {query}")

    result = ms.process_query(query)
    print(f"Detected Language: {result['language']}")
    print(f"Processed Text: {result['processed_text']}")
    print(f"Embedding Shape: {len(result['embedding'])}")

    if len(result["embedding"]) == 1024:
        print("✅ Embedding generated (1024 dim)")
    else:
        print(f"❌ Embedding dimension mismatch: {len(result['embedding'])}")


if __name__ == "__main__":
    test_language_detection()
    test_hindi_processing()
    test_multilingual_search_flow()

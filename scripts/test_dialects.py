import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.rag.multilingual_search import MultilingualSearch


def test_dialect(name: str, code: str, sample_text: str) -> None:
    print(f"\n--- Testing {name} ({code}) ---")

    search = MultilingualSearch()

    # Force the language code to test the specific processor
    # We bypass auto-detection for this test to verify the processor logic
    processor = search.processors.get(code)

    if not processor:
        print(f"❌ Processor for {code} not found!")
        return

    print(f"Processor: {processor.__class__.__name__}")

    # Test preprocessing
    result = processor.preprocess(sample_text)
    print(f"Original: {result['original']}")
    print(f"Processed: {result['processed_text']}")
    print(f"Tokens: {result['tokens']}")
    print("✅ Processor working")


if __name__ == "__main__":
    # Rajasthani
    test_dialect("Rajasthani", "raj", "म्हे जास्यां")

    # Haryanvi
    test_dialect("Haryanvi", "bgc", "ib ke karega")

    # Bhojpuri
    test_dialect("Bhojpuri", "bho", "ka hal ba")

    # Maithili
    test_dialect("Maithili", "mai", "ki hal aich")

    # Chhattisgarhi
    test_dialect("Chhattisgarhi", "hne", "tor name ka he")

    # Dogri
    test_dialect("Dogri", "doi", "tusa kiyan o")

    # Konkani
    test_dialect("Konkani", "kok", "tum koso asa")

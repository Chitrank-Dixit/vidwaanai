import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.graph.taxonomy_extractor import TaxonomyExtractor


def main():
    te = TaxonomyExtractor()
    text = "Krishna teaches Arjuna about Dharma and Karma Yoga."
    print(f"Text: {text}")
    results = te.extract(text)
    print(f"Found {len(results)} entities:")
    for e in results:
        print(f"- {e['name']} ({e['type']})")


if __name__ == "__main__":
    main()

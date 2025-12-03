from difflib import SequenceMatcher
from typing import Tuple, List, Dict
from src.core.logger import get_logger

logger = get_logger(__name__)


class FuzzyMatcher:
    def __init__(self, threshold: float = 0.8):
        self.threshold = threshold

    def similarity(self, text1: str, text2: str) -> float:
        """Calculate similarity between two texts"""
        return SequenceMatcher(None, text1.lower(), text2.lower()).ratio()

    def find_similar(self, query: str, corpus: list) -> list:
        """Find similar texts in corpus"""
        results = []

        for item in corpus:
            sim = self.similarity(query, item)
            if sim >= self.threshold:
                results.append({"item": item, "similarity": sim})

        return sorted(results, key=lambda x: x["similarity"], reverse=True)

    def correct_query(self, query: str, known_terms: list) -> str:
        """Correct query typos based on known terms"""
        if not known_terms:
            return query

        words = query.split()
        corrected = []

        for word in words:
            # Don't correct short words
            if len(word) < 4:
                corrected.append(word)
                continue

            matches = self.find_similar(word, known_terms)
            if (
                matches and matches[0]["similarity"] > 0.85
            ):  # High threshold for auto-correction
                best_match = matches[0]["item"]
                if best_match != word:
                    logger.info(f"Correcting typo: {word} -> {best_match}")
                corrected.append(best_match)
            else:
                corrected.append(word)

        return " ".join(corrected)

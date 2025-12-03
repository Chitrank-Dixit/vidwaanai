from typing import List

import regex

from src.language.language_processor import LanguageProcessor


class TamilProcessor(LanguageProcessor):
    def __init__(self) -> None:
        # Common Tamil stop words
        self.stop_words = set(
            [
                "ஒரு",
                "என்று",
                "மற்றும்",
                "இந்த",
                "இது",
                "என்ற",
                "கொண்டு",
                "அவர்",
                "நான்",
                "நீ",
                "நாம்",
                "அது",
                "அல்லது",
                "ஆனால்",
                "என",
                "ஆக",
            ]
        )

    def normalize(self, text: str) -> str:
        """Normalize Tamil text"""
        # Remove extra spaces
        normalized = regex.sub(r"\s+", " ", text).strip()
        return str(normalized)

    def tokenize(self, text: str) -> List[str]:
        """Tokenize Tamil text"""
        # Split on whitespace and punctuation
        tokens = regex.findall(r"\b\w+\b", text)
        return list(tokens)

    def remove_stopwords(self, tokens: List[str]) -> List[str]:
        """Remove Tamil stop words"""
        return [token for token in tokens if token.lower() not in self.stop_words]

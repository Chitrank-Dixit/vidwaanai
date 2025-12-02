from typing import List

import regex

from src.language.language_processor import LanguageProcessor


class KannadaProcessor(LanguageProcessor):
    def __init__(self) -> None:
        # Common Kannada stop words
        self.stop_words = set(
            [
                "ಮತ್ತು",
                "ಈ",
                "ಆ",
                "ಒಂದು",
                "ಅಲ್ಲಿ",
                "ಇಲ್ಲಿ",
                "ಹಾಗೂ",
                "ಅಥವಾ",
                "ನಾನು",
                "ನಾವು",
                "ನೀವು",
                "ಇದೆ",
                "ಆಗ",
                "ಈಗ",
                "ಬಗ್ಗೆ",
            ]
        )

    def normalize(self, text: str) -> str:
        """Normalize Kannada text"""
        # Remove extra spaces
        normalized = regex.sub(r"\s+", " ", text).strip()
        return str(normalized)

    def tokenize(self, text: str) -> List[str]:
        """Tokenize Kannada text"""
        # Split on whitespace and punctuation
        tokens = regex.findall(r"\b\w+\b", text)
        return list(tokens)

    def remove_stopwords(self, tokens: List[str]) -> List[str]:
        """Remove Kannada stop words"""
        return [token for token in tokens if token.lower() not in self.stop_words]

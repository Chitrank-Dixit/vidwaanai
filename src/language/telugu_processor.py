from src.language.language_processor import LanguageProcessor
import regex
from typing import List


class TeluguProcessor(LanguageProcessor):
    def __init__(self):
        # Common Telugu stop words
        self.stop_words = set(
            [
                "మరియు",
                "ఈ",
                "ఆ",
                "ఒక",
                "లో",
                "కు",
                "నుండి",
                "కోసం",
                "ద్వారా",
                "కాని",
                "లేదా",
                "నేను",
                "మేము",
                "మీరు",
                "ఉంది",
                "ఉన్నారు",
            ]
        )

    def normalize(self, text: str) -> str:
        """Normalize Telugu text"""
        # Remove extra spaces
        normalized = regex.sub(r"\s+", " ", text).strip()
        return normalized

    def tokenize(self, text: str) -> List[str]:
        """Tokenize Telugu text"""
        # Split on whitespace and punctuation
        tokens = regex.findall(r"\b\w+\b", text)
        return tokens

    def remove_stopwords(self, tokens: List[str]) -> List[str]:
        """Remove Telugu stop words"""
        return [token for token in tokens if token.lower() not in self.stop_words]

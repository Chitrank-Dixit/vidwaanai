from typing import List

import regex

from src.language.language_processor import LanguageProcessor


class GujaratiProcessor(LanguageProcessor):
    def __init__(self):
        # Common Gujarati stop words
        self.stop_words = set(
            [
                "છે",
                "અને",
                "તે",
                "તો",
                "પણ",
                "કે",
                "આ",
                "હું",
                "તમે",
                "માટે",
                "પર",
                "થી",
                "માં",
                "એ",
                "ને",
                "હોય",
                "કરે",
                "નથી",
            ]
        )

    def normalize(self, text: str) -> str:
        """Normalize Gujarati text"""
        # Remove extra spaces
        normalized = regex.sub(r"\s+", " ", text).strip()
        return normalized

    def tokenize(self, text: str) -> List[str]:
        """Tokenize Gujarati text"""
        # Split on whitespace and punctuation
        tokens = regex.findall(r"\b\w+\b", text)
        return tokens

    def remove_stopwords(self, tokens: List[str]) -> List[str]:
        """Remove Gujarati stop words"""
        return [token for token in tokens if token.lower() not in self.stop_words]

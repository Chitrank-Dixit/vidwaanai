from typing import List

import nltk
import regex

from src.language.language_processor import LanguageProcessor


class HindiProcessor(LanguageProcessor):
    def __init__(self):
        try:
            nltk.data.find("corpora/stopwords")
        except LookupError:
            nltk.download("stopwords")

        # Hindi stop words
        self.stop_words = set(
            [
                "है",
                "हैं",
                "का",
                "की",
                "के",
                "को",
                "में",
                "पर",
                "से",
                "और",
                "या",
                "यह",
                "वह",
                "इस",
                "उस",
                "जो",
                "क्या",
                "क्यों",
                "कहाँ",
                "कब",
                "कैसे",
                "तो",
                "भी",
            ]
        )

    def normalize(self, text: str) -> str:
        """Normalize Hindi text"""
        # Remove extra spaces
        normalized = regex.sub(r"\s+", " ", text).strip()
        return normalized

    def tokenize(self, text: str) -> List[str]:
        """Tokenize Hindi text"""
        # Split on whitespace and punctuation
        tokens = regex.findall(r"\b\w+\b", text)
        return tokens

    def remove_stopwords(self, tokens: List[str]) -> List[str]:
        """Remove Hindi stop words"""
        return [token for token in tokens if token.lower() not in self.stop_words]

    # Legacy support for existing calls (if any)
    def preprocess_hindi(self, text: str) -> dict:
        return self.preprocess(text)

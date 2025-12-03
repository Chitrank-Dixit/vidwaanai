import regex

from src.language.language_processor import LanguageProcessor


class MalayalamProcessor(LanguageProcessor):
    """Malayalam language processor"""

    def __init__(self):
        # Malayalam stop words (common words)
        self.stop_words = set(
            [
                "aanu",
                "aay",
                "aakam",
                "aakaram",
                "aayirunnu",
                "atha",
                "ee",
                "o",
                "kuttal",
                "enn",
                "ennanu",
                "injan",
                "a",
                "undayil",
                "undaya",
                "undakka",
                "vendu",
                "vendutal",
                "poleye",
                "maatram",
                "maaran",
                "valichey",
                "valecha",
                "nayan",
                "nayanu",
                "payyan",
                "oru",
                "njan",
                "ente",
                "ningal",
                "avar",
                "athu",
                "ithu",
                "ippol",
                "appol",
                "engane",
                "enthinu",
                "ethra",
            ]
        )

    def normalize(self, text: str) -> str:
        """Normalize Malayalam text"""
        # Remove diacritics/signs specific to Malayalam if needed
        # For now, we keep most marks as they are essential, but remove Zero Width Joiner/Non-Joiner
        normalized = regex.sub(r"[\u200C\u200D]", "", text)

        # Remove extra spaces
        normalized = regex.sub(r"\s+", " ", normalized).strip()

        return normalized

    def tokenize(self, text: str) -> list:
        """Tokenize Malayalam text"""
        # Malayalam uses word boundaries
        tokens = regex.findall(r"\b\w+\b", text)
        return tokens

    def remove_stopwords(self, tokens: list) -> list:
        """Remove Malayalam stop words"""
        return [token for token in tokens if token.lower() not in self.stop_words]

    def preprocess(self, text: str) -> dict:
        """Complete Malayalam preprocessing"""
        normalized = self.normalize(text)
        tokens = self.tokenize(normalized)
        filtered = self.remove_stopwords(tokens)

        return {
            "original": text,
            "normalized": normalized,
            "tokens": tokens,
            "filtered_tokens": filtered,
            "processed_text": " ".join(filtered),
        }

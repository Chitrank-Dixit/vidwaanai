import regex

from src.language.language_processor import LanguageProcessor


class BengaliProcessor(LanguageProcessor):
    """Bengali language processor"""

    def __init__(self):
        # Bengali stop words
        self.stop_words = set(
            [
                "aache",
                "aachen",
                "amar",
                "ami",
                "apnar",
                "apni",
                "ebam",
                "ete",
                "er",
                "ei",
                "oyi",
                "kintu",
                "ke",
                "kora",
                "korechhen",
                "korete",
                "kotha",
                "ekhon",
                "ek",
                "janya",
                "tar",
                "tara",
                "tini",
                "tumi",
                "te",
                "tyag",
                "dvara",
                "dbitiya",
                "na",
                "nie",
                "panchar",
                "pare",
                "panchha",
                "pash",
                "paewa",
                "post",
                "prati",
                "prayojan",
                "ray",
                "rakha",
                "rakheo",
                "rakshananda",
                "saddha",
                "sandhen",
                "sannden",
                "sara",
                "seraa",
                "shem",
                "sem",
                "sebaabhivichitta",
                "sheba",
                "semadhn",
                "sthan",
                "sthanei",
                "shvarupam",
                "haitei",
                "haowa",
                "hawayar",
                "hatei",
                "hate",
                "habe",
                "hebben",
                "haman",
                "hayam",
                "hayanchhen",
                "haye",
                "hayei",
                "harasda",
                "ykhon",
                "yak",
                "yakite",
                "yan",
                "yaa",
                "yaitei",
                "yai",
                "yainte",
                "yake",
                "yake",
                "yakei",
                "yajanya",
            ]
        )

    def normalize(self, text: str) -> str:
        """Normalize Bengali text"""
        # Remove Zero Width Joiner/Non-Joiner
        normalized = regex.sub(r"[\u200C\u200D]", "", text)

        # Remove extra spaces
        normalized = regex.sub(r"\s+", " ", normalized).strip()

        return normalized

    def tokenize(self, text: str) -> list:
        """Tokenize Bengali text"""
        tokens = regex.findall(r"\b\w+\b", text)
        return tokens

    def remove_stopwords(self, tokens: list) -> list:
        """Remove Bengali stop words"""
        return [token for token in tokens if token.lower() not in self.stop_words]

    def preprocess(self, text: str) -> dict:
        """Complete Bengali preprocessing"""
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

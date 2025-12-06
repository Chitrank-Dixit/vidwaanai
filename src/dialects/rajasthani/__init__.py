import json
import os
from typing import List, Dict, Any, Set

from src.language.language_processor import LanguageProcessor
from src.dialects.rajasthani.tokenizer import RajasthaniTokenizer
from src.dialects.rajasthani.normalizer import RajasthaniNormalizer


class RajasthaniProcessor(LanguageProcessor):
    """
    Comprehensive processor for Rajasthani language/dialect.
    Integrates normalization, tokenization, and stopword removal.
    """

    def __init__(self) -> None:
        self.tokenizer = RajasthaniTokenizer()
        self.normalizer = RajasthaniNormalizer()
        self.stop_words: Set[str] = set()
        self._load_resources()

    def _load_resources(self) -> None:
        """Load lexicon and stop words."""
        # Default stop words (migrated from legacy processor + expanded)
        default_stops = {
            "कोई",
            "कुई",
            "कूं",
            "कै",
            "नां",
            "ने",
            "सूं",
            "सो",
            "स्यो",
            "हो",
            "हुवो",
            "हिओ",
            "पण",
            "थे",
            "म्हे",
            "सा",
            "कोनी",
            "koni",
            "the",
            "mhe",
            "sa",
            "pan",
            "ho",
            "ne",
            "su",
        }
        self.stop_words.update(default_stops)

        # Try to load from lexicon file if exists
        lexicon_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "resources",
            "lexicons",
            "rajasthani_lexicon.json",
        )
        if os.path.exists(lexicon_path):
            try:
                with open(lexicon_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if "stop_words" in data:
                        self.stop_words.update(data["stop_words"])
            except Exception as e:
                print(f"Warning: Failed to load Rajasthani lexicon: {e}")

        # Load grammar
        grammar_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "resources",
            "grammars",
            "rajasthani_grammar.json",
        )
        self.grammar = {}
        if os.path.exists(grammar_path):
            try:
                with open(grammar_path, "r", encoding="utf-8") as f:
                    self.grammar = json.load(f)
            except Exception as e:
                print(f"Warning: Failed to load Rajasthani grammar: {e}")

    def normalize(self, text: str) -> str:
        """Normalize Rajasthani text."""
        return self.normalizer.normalize(text)

    def tokenize(self, text: str) -> List[str]:
        """Tokenize Rajasthani text."""
        return self.tokenizer.tokenize_words(text)

    def remove_stopwords(self, tokens: List[str]) -> List[str]:
        """Remove stop words."""
        return [t for t in tokens if t not in self.stop_words]

    def process(self, text: str) -> Dict[str, Any]:
        """
        Full processing pipeline.
        """
        return self.preprocess(text)

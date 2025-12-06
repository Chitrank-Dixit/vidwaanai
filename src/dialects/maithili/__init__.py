import json
import os
from typing import List, Dict, Any, Set

from src.language.language_processor import LanguageProcessor
from src.dialects.maithili.tokenizer import MaithiliTokenizer
from src.dialects.maithili.normalizer import MaithiliNormalizer
from src.dialects.maithili.morphology import MaithiliMorphologicalAnalyzer


class MaithiliProcessor(LanguageProcessor):
    """
    Comprehensive processor for Maithili language/dialect.
    Integrates normalization, tokenization, morphological analysis, and stopword removal.
    """

    def __init__(self) -> None:
        self.tokenizer = MaithiliTokenizer()
        self.normalizer = MaithiliNormalizer()
        self.morphology = MaithiliMorphologicalAnalyzer()
        self.stop_words: Set[str] = set()
        self._load_resources()

    def _load_resources(self) -> None:
        """Load lexicon and stop words."""
        # Default stop words (migrated from legacy processor + expanded)
        default_stops = {
            "chi",
            "achi",
            "aich",
            "chhai",
            "chhal",
            "hum",
            "aahan",
            "to",
            "ki",
            "je",
            "se",
            "me",
            "per",
            "le",
            "la",
            "k",
            "r",
            "अछि",
            "अइछ",
            "छै",
            "छल",
            "हम",
            "अहाँ",
            "त",
            "की",
            "जे",
            "से",
            "मे",
            "पर",
            "ले",
            "ला",
            "क",
            "र",
            "छी",
            "के",
        }
        self.stop_words.update(default_stops)

        # Try to load from lexicon file if exists
        lexicon_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "resources",
            "lexicons",
            "maithili_lexicon.json",
        )
        if os.path.exists(lexicon_path):
            try:
                with open(lexicon_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if "stop_words" in data:
                        self.stop_words.update(data["stop_words"])
            except Exception as e:
                print(f"Warning: Failed to load Maithili lexicon: {e}")

        # Load grammar
        grammar_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "resources",
            "grammars",
            "maithili_grammar.json",
        )
        self.grammar = {}
        if os.path.exists(grammar_path):
            try:
                with open(grammar_path, "r", encoding="utf-8") as f:
                    self.grammar = json.load(f)
            except Exception as e:
                print(f"Warning: Failed to load Maithili grammar: {e}")

    def normalize(self, text: str) -> str:
        """Normalize Maithili text."""
        return self.normalizer.normalize(text)

    def tokenize(self, text: str) -> List[str]:
        """Tokenize Maithili text."""
        return self.tokenizer.tokenize_words(text)

    def remove_stopwords(self, tokens: List[str]) -> List[str]:
        """Remove stop words."""
        return [t for t in tokens if t not in self.stop_words]

    def get_stem(self, word: str) -> str:
        """Get stem of a word."""
        return self.morphology.stem(word)

    def analyze_morphology(self, word: str) -> Dict[str, Any]:
        """Analyze morphology of a word."""
        return self.morphology.analyze(word)

    def process(self, text: str) -> Dict[str, Any]:
        """
        Full processing pipeline.
        """
        result = self.preprocess(text)
        # Add morphological analysis to result
        result["stems"] = [self.get_stem(t) for t in result["filtered_tokens"]]
        return result


class MaithiliDialectClassifier:
    """
    Classifier to distinguish Maithili dialects (Sotipura, Bajjik, Angika).
    Currently a stub/placeholder.
    """

    def __init__(self) -> None:
        # Dialect markers
        self.markers = {
            "Sotipura (Standard)": {
                "अछि",
                "छी",
                "अइछ",
                "हम",
                "अहाँ",
                "की",
                "जे",
                "से",
                "क",
                "र",
            },
            "Angika": {"छै", "छौ", "छे", "हमर", "तोहर", "क", "र"},
            "Bajjika": {"बा", "हई", "रउआ", "त", "मुदा"},
        }

    def classify(self, text: str) -> str:
        """
        Classify Maithili text into a dialect.
        Returns: 'Sotipura (Standard)', 'Angika', 'Bajjika', or 'Standard Maithili' (default).
        """
        if not text:
            return "Standard Maithili"

        scores = {dialect: 0 for dialect in self.markers}
        words = text.split()

        for word in words:
            for dialect, markers in self.markers.items():
                if word in markers:
                    scores[dialect] += 1

        # Get dialect with max score
        best_dialect = max(scores, key=lambda k: scores[k])

        if scores[best_dialect] > 0:
            return best_dialect
        return "Standard Maithili"

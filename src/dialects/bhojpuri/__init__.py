import json
import os
from typing import List, Dict, Any, Set

from src.language.language_processor import LanguageProcessor
from src.dialects.bhojpuri.tokenizer import BhojpuriTokenizer
from src.dialects.bhojpuri.normalizer import BhojpuriNormalizer
from src.dialects.bhojpuri.morphology import BhojpuriMorphologicalAnalyzer
from src.dialects.bhojpuri.stress import BhojpuriStressAnalyzer


class BhojpuriProcessor(LanguageProcessor):
    """
    Comprehensive processor for Bhojpuri language/dialect.
    Integrates normalization, tokenization, morphological analysis, stress analysis, and stopword removal.
    Supports Northern, Southern, and Western dialects.
    """

    def __init__(self) -> None:
        self.tokenizer = BhojpuriTokenizer()
        self.normalizer = BhojpuriNormalizer()
        self.morphology = BhojpuriMorphologicalAnalyzer()
        self.stress_analyzer = BhojpuriStressAnalyzer()
        self.stop_words: Set[str] = set()
        self._load_resources()

    def _load_resources(self) -> None:
        """Load lexicon and stop words."""
        # Default stop words (migrated from legacy processor + expanded)
        default_stops = {
            "ba",
            "bate",
            "bari",
            "ho",
            "raua",
            "hamar",
            "tohar",
            "ka",
            "ke",
            "ki",
            "se",
            "me",
            "par",
            "ne",
            "bani",
            "bhayil",
            "rah",
            "ja",
            "aa",
            "na",
            "बा",
            "बाटे",
            "बारी",
            "हो",
            "रउआ",
            "हमर",
            "तोहर",
            "का",
            "के",
            "की",
            "से",
            "मे",
            "पर",
            "ने",
            "बानी",
            "भइल",
            "रह",
            "जा",
            "आ",
            "ना",
            "ई",
            "ऊ",
        }
        self.stop_words.update(default_stops)

        # Try to load from lexicon file if exists
        lexicon_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "resources",
            "lexicons",
            "bhojpuri_lexicon.json",
        )
        if os.path.exists(lexicon_path):
            try:
                with open(lexicon_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if "stop_words" in data:
                        self.stop_words.update(data["stop_words"])
            except Exception as e:
                print(f"Warning: Failed to load Bhojpuri lexicon: {e}")

        # Load grammar
        grammar_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "resources",
            "grammars",
            "bhojpuri_grammar.json",
        )
        self.grammar = {}
        if os.path.exists(grammar_path):
            try:
                with open(grammar_path, "r", encoding="utf-8") as f:
                    self.grammar = json.load(f)
            except Exception as e:
                print(f"Warning: Failed to load Bhojpuri grammar: {e}")

    def normalize(self, text: str) -> str:
        """Normalize Bhojpuri text."""
        return self.normalizer.normalize(text)

    def tokenize(self, text: str) -> List[str]:
        """Tokenize Bhojpuri text."""
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

    def analyze_stress(self, word: str) -> int:
        """Get the index of the stressed syllable."""
        return self.stress_analyzer.analyze(word)

    def process(self, text: str) -> Dict[str, Any]:
        """
        Full processing pipeline.
        """
        result = self.preprocess(text)
        # Add morphological analysis to result
        result["stems"] = [self.get_stem(t) for t in result["filtered_tokens"]]
        # Add stress info (optional, maybe just for specific words if needed)
        # For now, let's just expose the method.
        return result


class BhojpuriDialectClassifier:
    """
    Classifier to distinguish Bhojpuri dialects (Northern, Southern, Western).
    Currently a stub/placeholder.
    """

    def __init__(self) -> None:
        # Dialect markers
        self.markers = {
            "Southern (Standard)": {"बा", "बानी", "रउआ", "का", "के", "की", "हो"},
            "Northern": {"बाटे", "बा", "बटे", "काहे", "कि"},
            "Western": {"हौ", "है", "का", "त", "ना"},
        }

    def classify(self, text: str) -> str:
        """
        Classify Bhojpuri text into a dialect.
        Returns: 'Southern (Standard)', 'Northern', 'Western', or 'Standard Bhojpuri' (default).
        """
        if not text:
            return "Standard Bhojpuri"

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
        return "Standard Bhojpuri"

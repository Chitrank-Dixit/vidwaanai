from typing import Dict, Any


class MaithiliMorphologicalAnalyzer:
    """
    Morphological Analyzer for Maithili.
    Handles stemming and basic morphological analysis.
    """

    def __init__(self) -> None:
        # Common suffixes for Maithili verbs and nouns
        # This is a simplified rule set.
        self.suffixes = [
            ("छि", "be"),  # chi (am)
            ("अछि", "be"),  # achi (is)
            ("छै", "be"),  # chhai (is)
            ("ल", "past"),  # -l (past tense marker)
            ("ब", "future"),  # -b (future tense marker)
            ("क", "genitive"),  # -k (of)
            ("सँ", "ablative"),  # -san (from)
            ("मे", "locative"),  # -me (in)
        ]

    def analyze(self, word: str) -> Dict[str, Any]:
        """
        Analyze a word for its root and grammatical features.

        Args:
            word: Input word

        Returns:
            Dictionary with 'root', 'suffix', 'category'
        """
        if not word:
            return {"root": "", "suffix": "", "category": "unknown"}

        for suffix, category in self.suffixes:
            if word.endswith(suffix) and len(word) > len(suffix):
                return {
                    "root": word[: -len(suffix)],
                    "suffix": suffix,
                    "category": category,
                }

        return {"root": word, "suffix": "", "category": "unknown"}

    def stem(self, word: str) -> str:
        """Return the stem of the word."""
        analysis = self.analyze(word)
        return str(analysis["root"])

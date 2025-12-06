from typing import Dict, Any


class BhojpuriMorphologicalAnalyzer:
    """
    Morphological Analyzer for Bhojpuri.
    Handles stemming and basic morphological analysis.
    """

    def __init__(self) -> None:
        # Common suffixes for Bhojpuri verbs and nouns
        # Simplified rule set.
        self.suffixes = [
            ("बानी", "be"),  # bani (am/are)
            ("बा", "be"),  # ba (is)
            ("बाटे", "be"),  # bate (is)
            ("ल", "past"),  # -l (past tense marker)
            ("ब", "future"),  # -b (future tense marker)
            ("के", "genitive"),  # -ke (of/to)
            ("से", "ablative"),  # -se (from)
            ("में", "locative"),  # -me (in)
            ("न", "negation"),  # -na (not/no)
            ("सन", "plural"),  # -san (plural marker sometimes)
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

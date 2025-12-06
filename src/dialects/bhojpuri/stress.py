import regex
from typing import List


class BhojpuriStressAnalyzer:
    """
    Analyzes stress patterns in Bhojpuri words.
    Based on weight-sensitive stress rules.
    """

    def __init__(self) -> None:
        # Long vowels (Guru)
        self.long_vowels = set("आ ई ऊ ए ऐ ओ औ".split())
        # Short vowels (Laghu)
        self.short_vowels = set("अ इ उ ऋ".split())

    def get_syllables(self, word: str) -> List[str]:
        """
        Split word into syllables.
        This is a simplified syllabification for Devanagari.
        """
        # Regex to match a consonant+vowel or independent vowel
        # This is an approximation.
        # Pattern: (Consonant+Matra? | Vowel)
        pattern = r"[\u0905-\u0939][\u093e-\u094c]?|[\u0905-\u0914]"
        return [str(match) for match in regex.findall(pattern, word)]

    def is_heavy(self, syllable: str) -> bool:
        """Check if a syllable is heavy (Guru)."""
        # Check for long vowel matras or independent long vowels
        for char in syllable:
            if char in self.long_vowels:
                return True
            # Check matras
            if char in [
                "\u093e",
                "\u0940",
                "\u0942",
                "\u0947",
                "\u0948",
                "\u094b",
                "\u094c",
            ]:
                return True
        return False

    def analyze(self, word: str) -> int:
        """
        Identify the index of the stressed syllable (0-indexed).
        Rule: Stress falls on the heaviest syllable among the last three.
        If equal, rightmost wins (simplified).
        """
        syllables = self.get_syllables(word)
        if not syllables:
            return -1

        # Analyze last 3 syllables
        candidates = syllables[-3:]
        offset = len(syllables) - len(candidates)

        # Find rightmost heavy syllable
        for i in range(len(candidates) - 1, -1, -1):
            if self.is_heavy(candidates[i]):
                return offset + i

        # Default to penultimate if exists, else first
        if len(syllables) > 1:
            return len(syllables) - 2
        return 0

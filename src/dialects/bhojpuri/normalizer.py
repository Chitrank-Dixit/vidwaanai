import regex
from typing import Dict


class BhojpuriNormalizer:
    """
    Normalizer for Bhojpuri text.
    Handles Devanagari normalization and Bhojpuri-specific characters like Avagraha.
    """

    def __init__(self) -> None:
        # Common normalization maps
        self.normalization_map: Dict[str, str] = {
            "\u200c": "",  # Zero Width Non-Joiner
            "\u200d": "",  # Zero Width Joiner
            # Nukta characters normalization (similar to Hindi/Maithili)
            "\u0958": "\u0915\u093c",  # qa
            "\u0959": "\u0916\u093c",  # kha
            "\u095a": "\u0917\u093c",  # gha
            "\u095b": "\u091c\u093c",  # za
            "\u095c": "\u0921\u093c",  # dddha
            "\u095d": "\u0922\u093c",  # rha
            "\u095e": "\u0924\u093c",  # fa
            "\u095f": "\u092f\u093c",  # yya
        }

    def normalize(self, text: str) -> str:
        """
        Normalize Bhojpuri text.

        Args:
            text: Input text string

        Returns:
            Normalized text string
        """
        if not text:
            return ""

        # 1. Character replacement
        normalized = text
        for char, replacement in self.normalization_map.items():
            normalized = normalized.replace(char, replacement)

        # 2. Avagraha (ऽ) handling
        # In Bhojpuri, Avagraha represents a drawled vowel.
        # We generally keep it, but ensure it's the correct unicode character (U+093D).
        # Some texts might use 'S' or other symbols.
        normalized = normalized.replace(
            "S", "\u093d"
        )  # Replace Latin S if used as Avagraha (heuristic)

        # 3. Whitespace normalization
        normalized = str(regex.sub(r"\s+", " ", normalized)).strip()

        return normalized

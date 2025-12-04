import regex
from typing import Dict


class RajasthaniNormalizer:
    """
    Normalizer for Rajasthani text.
    Handles Devanagari normalization.
    """

    def __init__(self) -> None:
        # Common normalization maps
        self.normalization_map: Dict[str, str] = {
            "\u200c": "",  # Zero Width Non-Joiner
            "\u200d": "",  # Zero Width Joiner
            # Nukta characters normalization
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
        Normalize Rajasthani text.

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

        # 2. Whitespace normalization
        normalized = str(regex.sub(r"\s+", " ", normalized)).strip()

        return normalized

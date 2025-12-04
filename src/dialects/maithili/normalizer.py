import regex
from typing import Dict


class MaithiliNormalizer:
    """
    Normalizer for Maithili text.
    Handles Devanagari normalization and Maithili-specific characters.
    """

    def __init__(self) -> None:
        # Common normalization maps
        self.normalization_map: Dict[str, str] = {
            "\u200c": "",  # Zero Width Non-Joiner
            "\u200d": "",  # Zero Width Joiner
            "\u0958": "\u0915\u093c",  # qa -> ka + nukta
            "\u0959": "\u0916\u093c",  # kha -> kha + nukta
            "\u095a": "\u0917\u093c",  # gha -> gha + nukta
            "\u095b": "\u091c\u093c",  # za -> ja + nukta
            "\u095c": "\u0921\u093c",  # dddha -> dda + nukta
            "\u095d": "\u0922\u093c",  # rha -> dda + nukta
            "\u095e": "\u0924\u093c",  # fa -> pha + nukta
            "\u095f": "\u092f\u093c",  # yya -> ya + nukta
        }

    def normalize(self, text: str) -> str:
        """
        Normalize Maithili text.

        Args:
            text: Input text string

        Returns:
            Normalized text string
        """
        if not text:
            return ""

        # 1. Unicode Normalization (NFC)
        # (Python strings are usually unicode, but explicit normalization is good practice)
        # For now, we assume input is decent unicode.

        # 2. Character replacement
        normalized = text
        for char, replacement in self.normalization_map.items():
            normalized = normalized.replace(char, replacement)

        # 3. Whitespace normalization
        normalized = str(regex.sub(r"\s+", " ", normalized)).strip()

        # 4. Maithili specific: Chandra Bindu normalization (often interchangeable with Anusvara in informal text)
        # But in standard Maithili, they are distinct. We keep them distinct for now unless requested otherwise.

        # 5. Remove punctuation (optional, usually done in tokenization or separate step)
        # Here we keep punctuation for structure preservation.

        return normalized

from langdetect import detect
import re


class TextProcessor:
    """Process Veda texts (Hindi/Sanskrit)."""

    def detect_language(self, text: str) -> str:
        """Detect if Hindi or Sanskrit."""
        try:
            lang = detect(text)
            return "hi" if lang == "hi" else "sa"
        except Exception:
            return "unknown"

    def clean_text(self, text: str) -> str:
        """Clean OCR artifacts, normalize text."""
        if not text:
            return ""
        # Remove extra whitespace
        text = re.sub(r"\s+", " ", text)
        # Remove page numbers (simple heuristic)
        text = re.sub(r"Page \d+", "", text)
        # Normalize Devanagari
        text = self.normalize_devanagari(text)
        return text.strip()

    def normalize_devanagari(self, text: str) -> str:
        """Normalize variations in Devanagari script."""
        # Handle common OCR errors
        replacements = {
            "०": "0",
            "१": "1",
            "२": "2",
            "३": "3",
            "४": "4",
            "५": "5",
            "६": "6",
            "७": "7",
            "८": "8",
            "९": "9",
            "ऽ": "ा",  # Common OCR confusion
        }
        for src, dst in replacements.items():
            text = text.replace(src, dst)
        return text

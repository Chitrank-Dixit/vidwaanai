from typing import Dict, List, Any
from langdetect import detect, detect_langs

# Supported languages in VidwaanAI
SUPPORTED_LANGUAGES = {
    "hi": "Hindi",
    "ta": "Tamil",
    "te": "Telugu",
    "kn": "Kannada",
    "ml": "Malayalam",
    "bn": "Bengali",
    "en": "English",
}


def detect_language(query: str) -> Dict[str, Any]:
    """
    Detects the language of the given query.

    Args:
        query: The input text to analyze.

    Returns:
        A dictionary containing the detected language code, name, and confidence score.
    """
    try:
        langs = detect_langs(query)
        best_match = langs[0]
        lang_code = best_match.lang
        confidence = best_match.prob

        # Map to full name if supported, else use code
        lang_name = SUPPORTED_LANGUAGES.get(lang_code, "Unknown")

        return {
            "language_code": lang_code,
            "language_name": lang_name,
            "confidence": confidence,
            "is_supported": lang_code in SUPPORTED_LANGUAGES,
        }
    except Exception as e:
        return {
            "language_code": "unknown",
            "language_name": "Unknown",
            "confidence": 0.0,
            "error": str(e),
            "is_supported": False,
        }


def preprocess_text(text: str, language: str = "en") -> Dict[str, Any]:
    """
    Preprocesses the text based on the specified language.

    Args:
        text: The input text to preprocess.
        language: The language code (e.g., 'hi', 'en').

    Returns:
        A dictionary containing the normalized text and tokens.
    """
    # Basic preprocessing for now - can be expanded with specific language logic
    normalized = text.strip().lower()

    # Simple tokenization (split by whitespace)
    # In a real scenario, we'd use language-specific tokenizers
    tokens = normalized.split()

    return {
        "original_text": text,
        "normalized_text": normalized,
        "tokens": tokens,
        "token_count": len(tokens),
        "language": language,
    }


def get_supported_languages() -> List[Dict[str, str]]:
    """
    Returns a list of supported languages.

    Returns:
        A list of dictionaries with language code and name.
    """
    return [{"code": k, "name": v} for k, v in SUPPORTED_LANGUAGES.items()]

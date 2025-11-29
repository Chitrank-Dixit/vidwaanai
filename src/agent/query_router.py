"""Query routing and language detection."""

from typing import Dict, Optional
import logging

logger = logging.getLogger(__name__)


class QueryRouter:
    """Routes queries based on language and content."""

    def detect_language(self, text: str) -> Optional[str]:
        """Detect language of text using Unicode ranges."""
        for char in text:
            code = ord(char)
            if 0x0900 <= code <= 0x097F:  # Devanagari (Hindi)
                return "hi"
            elif 0x0B80 <= code <= 0x0BFF:  # Tamil
                return "ta"
            elif 0x0C00 <= code <= 0x0C7F:  # Telugu
                return "te"
            elif 0x0D00 <= code <= 0x0D7F:  # Malayalam
                return "ml"
            elif 0x0C80 <= code <= 0x0CFF:  # Kannada
                return "kn"
        return None

    def route_query(
        self, question: str, language: str, scripture_filter: Optional[str] = None
    ) -> Dict:
        """Route query with filtering strategy."""
        return {
            "language": language,
            "use_metadata_filter": scripture_filter is not None,
            "scripture_filter": scripture_filter,
            "retrieval_mode": "hybrid",
            "top_k": 5,
        }

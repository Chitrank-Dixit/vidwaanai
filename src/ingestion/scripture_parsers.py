import re
import logging
from typing import List, Dict, Optional, Any

logger = logging.getLogger(__name__)


class BaseScriptureParser:
    """Base class for parsing varying scripture structures."""

    PATTERNS: Dict[str, Optional[str]] = {
        "l1_node": r"",  # Top level (Mandala, Kanda, Skanda)
        "l2_node": r"",  # Mid level (Sukta, Sarga, Adhyaya)
        "verse": r"",  # Verse level (Mantra, Shloka)
    }

    def __init__(self) -> None:
        self.current_l1 = 0
        self.current_l2 = 0
        self.verse_count = 0

    def parse(self, pages: List[Dict[str, Any]], code: str) -> List[Dict[str, Any]]:
        """Parse pages into verse structure."""
        verses = []
        self.current_l1 = 0
        self.current_l2 = 0
        self.verse_count = 0

        for page in pages:
            text = page["text"]

            # L1 Node Detection
            if self.PATTERNS["l1_node"]:
                match = re.search(self.PATTERNS["l1_node"], text, re.IGNORECASE)
                if match:
                    try:
                        self.current_l1 = int(match.group(1))
                        # Reset child counters if needed, though usually sequential
                    except ValueError:
                        pass

            # L2 Node Detection
            if self.PATTERNS["l2_node"]:
                match = re.search(self.PATTERNS["l2_node"], text, re.IGNORECASE)
                if match:
                    try:
                        self.current_l2 = int(match.group(1))
                    except ValueError:
                        pass

            # Verse splitting
            blocks = self._split_verses(text)

            for block in blocks:
                if not block.strip():
                    continue

                self.verse_count += 1
                verses.append(
                    {
                        "ved_code": code,
                        "mandala_id": self.current_l1,  # Mapped to L1
                        "sukta_id": self.current_l2,  # Mapped to L2
                        "mantra_number": self.verse_count,
                        "text": block.strip(),
                        "translation": "",
                        "tags": self._extract_tags(block),
                    }
                )

        logger.info(f"Parsed {len(verses)} verses")
        return verses

    def _split_verses(self, text: str) -> List[str]:
        """Split text into individual verses."""
        # Standard splitting by double danda (||) common in Sanskrit
        # Also handle potential 'Mantra X' headers if defined

        # Default split logic
        chunks = re.split(r"(?:[\॥\|]{1,2})", text)
        return [c.strip() for c in chunks if len(c.strip()) > 5]

    def _extract_tags(self, text: str) -> List[str]:
        """Tag extraction - can overlap with VedaParser logic."""
        tags = []
        keywords = {
            "dharma": ["धर्म", "कर्तव्य", "सत्य", "न्याय"],
            "karma": ["कर्म", "फल", "क्रिया", "प्रयास"],
            "bhakti": ["भक्ति", "प्रेम", "समर्पण", "श्रद्धा", "पूजा"],
            "war": ["युद्ध", "शस्त्र", "बाण", "सेना", "वीर"],
            "knowledge": ["ज्ञान", "विद्या", "बोध", "शास्त्र"],
            "nature": ["वन", "नदी", "पर्वत", "सूर्य", "चन्द्र"],
        }
        for cat, kws in keywords.items():
            if any(k in text for k in kws):
                tags.append(cat)
        return list(set(tags))


class GitaParser(BaseScriptureParser):
    """Parser for Bhagavad Gita."""

    def __init__(self) -> None:
        super().__init__()
        self.PATTERNS = {
            "l1_node": r"अध्याय\s*[:=]?\s*(\d+)",  # Adhyaya -> Mandala
            "l2_node": None,  # No sub-level -> Sukta 0
            "verse": r"श्लोक\s*[:=]?\s*(\d+)",
        }

    def _split_verses(self, text: str) -> List[str]:
        # Gita verses often labeled 'श्लोक X' or just text with ||
        # For now, default danda split, but maybe prioritize 'श्लोक' header
        return super()._split_verses(text)


class RamayanaParser(BaseScriptureParser):
    """Parser for Ramayana."""

    def __init__(self) -> None:
        super().__init__()
        self.PATTERNS = {
            "l1_node": r"काण्ड\s*[:=]?\s*(\d+)",  # Kanda -> Mandala
            "l2_node": r"सर्ग\s*[:=]?\s*(\d+)",  # Sarga -> Sukta
            "verse": None,
        }


class PuranaParser(BaseScriptureParser):
    """Parser for Puranas."""

    def __init__(self) -> None:
        super().__init__()
        self.PATTERNS = {
            "l1_node": r"(?:स्कन्ध|खण्ड)\s*[:=]?\s*(\d+)",  # Skanda/Khanda -> Mandala
            "l2_node": r"अध्याय\s*[:=]?\s*(\d+)",  # Adhyaya -> Sukta
            "verse": None,
        }


class MahabharatParser(BaseScriptureParser):
    """Parser for Mahabharat."""

    def __init__(self) -> None:
        super().__init__()
        self.PATTERNS = {
            "l1_node": r"पर्व\s*[:=]?\s*(\d+)",  # Parva -> Mandala
            "l2_node": r"अध्याय\s*[:=]?\s*(\d+)",  # Adhyaya -> Sukta
            "verse": None,
        }


def get_parser(scripture_type: str) -> BaseScriptureParser:
    """Factory method."""
    t = scripture_type.lower()
    if t == "gita":
        return GitaParser()
    elif t == "ramayana":
        return RamayanaParser()
    elif t == "mahabharat":
        return MahabharatParser()
    elif t == "purana":
        return PuranaParser()
    else:
        # Default or Veda
        from src.ingestion.veda_parser import VedaParser

        # VedaParser matches the interface but is standalone.
        # Ideally we wrap it or return it if interfaces align.
        # VedaParser.parse_vedas signature is same.
        # We need to adapt VedaParser to BaseScriptureParser interface or cast it
        # Since VedaParser is different, let's allow return type Union or cast
        from typing import cast

        # For now, suppressing type error or assuming VedaParser will be refactored to inherit
        # cast(BaseScriptureParser, VedaParser())
        return cast(BaseScriptureParser, VedaParser())

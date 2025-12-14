import re
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)


class VedaParser:
    """Parse Veda structure from text."""

    PATTERNS = {
        "mandala": r"मंडल\s*[:=]?\s*(\d+)",  # Mandala number
        "sukta": r"सूक्त\s*[:=]?\s*(\d+)",  # Sukta number
        "mantra": r"मंत्र\s*[:=]?\s*(\d+)",  # Mantra number
    }

    def parse_vedas(self, pages: List[Dict], ved_code: str) -> List[Dict]:
        """Parse pages into mantra structure."""
        mantras = []
        current_mandala = 0
        current_sukta = 0
        mantra_count = 0

        # Rig Veda uses Mandalas. Others might use Kanda/Adhyaya but we map to similar hierarchy
        # Using a flat iteration over pages might miss context if a mandala spans pages
        # But usually headers are repeated or distinct enough.

        for page in pages:
            text = page["text"]

            # Extract mandala (update current context if found)
            mandala_match = re.search(self.PATTERNS["mandala"], text)
            if mandala_match:
                try:
                    current_mandala = int(mandala_match.group(1))
                except ValueError:
                    pass

            # Extract sukta
            sukta_match = re.search(self.PATTERNS["sukta"], text)
            if sukta_match:
                try:
                    current_sukta = int(sukta_match.group(1))
                except ValueError:
                    pass

            # Split into individual mantras
            mantra_blocks = self._split_mantras(text)

            for block in mantra_blocks:
                if not block.strip():
                    continue

                # Try to extract explicit mantra number if present at start
                # Validation logic could go here

                mantra_count += 1
                mantras.append(
                    {
                        "ved_code": ved_code,
                        "mandala_id": current_mandala,
                        "sukta_id": current_sukta,
                        "mantra_number": mantra_count,
                        "text": block.strip(),
                        "translation": "",  # Filled from external source or adjacent text if available
                        "tags": self._extract_tags(block),
                    }
                )

        logger.info(f"Parsed {len(mantras)} mantras for {ved_code}")
        return mantras

    def _split_mantras(self, text: str) -> List[str]:
        """Split text into individual mantras."""
        # Split by common delimiters like double danda (||) or explicit 'Mantra' labels
        # The regex splits by 'मंत्र' keyword or danda punctuation, keeping the delimiter if needed?
        # A simple split usually consumes the delimiter.
        # Let's try splitting by double danda which is standard in Sanskrit texts

        # Regex:
        # (?: ... ) is non-capturing group
        # मंत्र\s*\d+ matches "Mantra 1" etc
        # ।{1,2} matches | or ||

        chunks = re.split(r"(?:मंत्र\s*\d+[:\.]?|[\॥\|]{1,2})", text)
        return [
            c.strip() for c in chunks if len(c.strip()) > 5
        ]  # Lower filter to 5 chars to match test data

    def _extract_tags(self, text: str) -> List[str]:
        """Extract keywords/tags from mantra."""
        tags = []
        # Basic keyword mapping - can be expanded
        keywords = {
            "health": ["औषधि", "रोग", "चिकित्सा", "तंदुरुस्त", "आयु"],
            "ritual": ["यज्ञ", "अग्नि", "हवि", "पूजन", "अनुष्ठान", "सोम"],
            "nature": ["इंद्र", "वायु", "सूर्य", "जल", "पृथ्वी", "नदी", "पर्वत", "उषा"],
            "wisdom": ["ब्रह्म", "ज्ञान", "विद्या", "बुद्धि", "सत्य", "मन"],
            "divine": ["देव", "ईश्वर", "परमात्मा", "वरुण", "मित्र"],
            "family": ["पिता", "माता", "पुत्र", "गृह", "पारिवार"],
            "prosperity": ["धन", "लक्ष्मी", "समृद्धि", "गो", "अश्व"],
        }

        for category, keywords_list in keywords.items():
            if any(kw in text for kw in keywords_list):
                tags.append(category)

        return list(set(tags))  # unique tags

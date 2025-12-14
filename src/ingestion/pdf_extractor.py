from pypdf import PdfReader
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)


class PdfExtractor:
    """Extract text from Veda PDFs (Hindi)."""

    def extract_pdf(self, pdf_path: str) -> List[str]:
        """Extract all text from PDF."""
        reader = PdfReader(pdf_path)
        pages = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pages.append(text)
        return pages

    def extract_with_metadata(self, pdf_path: str) -> List[Dict]:
        """Extract text with page metadata."""
        try:
            reader = PdfReader(pdf_path)
            results = []
            for page_num, page in enumerate(reader.pages):
                text = page.extract_text()
                results.append(
                    {"page": page_num + 1, "text": text or "", "source": pdf_path}
                )
            return results
        except Exception as e:
            logger.error(f"Error extracting PDF {pdf_path}: {e}")
            raise

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

    def extract_with_metadata(self, pdf_path: str, max_pages: int = None) -> List[Dict]:
        """Extract text with page metadata. Fallback to OCR if empty."""
        try:
            reader = PdfReader(pdf_path)
            results = []
            total_text_len = 0

            total_pages = len(reader.pages)
            logger.info(f"Extracting {total_pages} pages from {pdf_path}...")

            for page_num, page in enumerate(reader.pages):
                if max_pages and page_num >= max_pages:
                    break

                if (page_num + 1) % 10 == 0:
                    logger.info(f"  -> Extracting page {page_num + 1}/{total_pages}...")

                text = page.extract_text() or ""
                total_text_len += len(text.strip())
                results.append({"page": page_num + 1, "text": text, "source": pdf_path})

            # Heuristic: If we extracted almost no text (< 100 chars total), try OCR
            if total_text_len < 100:
                logger.warning(
                    f"No text extracted from {pdf_path} (len={total_text_len}). Attempting OCR..."
                )
                try:
                    from src.ingestion.ocr_handler import OCRHandler

                    ocr = OCRHandler()
                    return ocr.extract_text_with_ocr(pdf_path, max_pages=max_pages)
                except ImportError:
                    logger.error("OCR dependencies missing. Returning empty text.")
                except Exception as e:
                    logger.error(f"OCR fallback failed: {e}")

            return results
        except Exception as e:
            logger.error(f"Error extracting PDF {pdf_path}: {e}")
            raise

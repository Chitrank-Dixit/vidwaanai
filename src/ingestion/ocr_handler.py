from typing import List, Dict
import logging

try:
    from pdf2image import convert_from_path
    import pytesseract
except ImportError:
    convert_from_path = None
    pytesseract = None

logger = logging.getLogger(__name__)


class OCRHandler:
    """Handle OCR for scanned Veda PDFs."""

    def __init__(self):
        if not convert_from_path or not pytesseract:
            logger.warning("OCR dependencies not installed (pdf2image, pytesseract).")

    def extract_text_with_ocr(self, pdf_path: str, lang: str = "hin") -> List[Dict]:
        """Convert PDF pages to images and extract text using OCR."""
        if not convert_from_path:
            raise ImportError("pdf2image not installed")

        try:
            images = convert_from_path(pdf_path)
            results = []

            for i, image in enumerate(images):
                text = pytesseract.image_to_string(image, lang=lang)
                results.append(
                    {"page": i + 1, "text": text, "source": pdf_path, "method": "ocr"}
                )
            return results

        except Exception as e:
            logger.error(f"OCR failed for {pdf_path}: {e}")
            raise

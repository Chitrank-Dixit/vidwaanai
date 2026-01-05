from typing import List, Dict, Optional, Any
import logging

try:
    from pdf2image import convert_from_path
    import pytesseract
except ImportError:
    convert_from_path = None  # type: ignore
    pytesseract = None

# Handle optional imports for mypy
if convert_from_path is None:
    pass  # Allow mypy to see it can be None



logger = logging.getLogger(__name__)


class OCRHandler:
    """Handle OCR for scanned Veda PDFs."""

    def __init__(self) -> None:
        if convert_from_path is None or pytesseract is None:
            logger.warning("OCR dependencies not installed (pdf2image, pytesseract).")

    def extract_text_with_ocr(
        self, pdf_path: str, lang: str = "hin", max_pages: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """Convert PDF pages to images and extract text using OCR (batched)."""
        if convert_from_path is None:
            raise ImportError("pdf2image not installed")

        results: List[Dict[str, Any]] = []
        try:
            # Process in batches of 10 pages to avoid OOM
            # We don't know total pages easily without reading, so we iterate until no images returned?
            # actually convert_from_path reads the whole file unless we specify first/last_page.
            # We need to know page count to loop efficiently.
            from pypdf import PdfReader

            total_pdf_pages = len(PdfReader(pdf_path).pages)

            processing_limit = total_pdf_pages
            if max_pages and max_pages < total_pdf_pages:
                processing_limit = max_pages

            batch_size = 5
            for start_page in range(1, processing_limit + 1, batch_size):
                end_page = min(start_page + batch_size - 1, processing_limit)

                logger.info(
                    f"OCR Processing pages {start_page}-{end_page} of {processing_limit}..."
                )

                images = convert_from_path(
                    pdf_path, first_page=start_page, last_page=end_page
                )

                for i, image in enumerate(images):
                    # Timeout after 30s per page
                    text = pytesseract.image_to_string(image, lang=lang, timeout=30)
                    results.append(
                        {
                            "page": start_page + i,
                            "text": text,
                            "source": pdf_path,
                            "method": "ocr",
                        }
                    )

            return results

        except Exception as e:
            logger.error(f"OCR failed for {pdf_path}: {e}")
            raise

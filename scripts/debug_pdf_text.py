import sys
import os
import logging

# Add src to python path to ensure imports work
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.ingestion.pdf_extractor import PdfExtractor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def debug_pdf(file_path):
    print(f"\n\n--- ANALYZING: {file_path} ---")
    if not os.path.exists(file_path):
        print("File not found.")
        return

    extractor = PdfExtractor()
    pages = extractor.extract_pdf(file_path)

    if not pages:
        print("No text found. Trying OCR...")
        try:
            from src.ingestion.ocr_handler import OCRHandler

            ocr = OCRHandler()
            ocr.extract_text_with_ocr(file_path)
            # Just take text from OCR results
            # Warning: OCR is slow, let's limit to first 1 page
            from pdf2image import convert_from_path
            import pytesseract

            print("Converting PDF to image (page 1)...")
            images = convert_from_path(file_path, first_page=1, last_page=1)
            pages = []
            print("Running Tesseract OCR on page 1...")
            for img in images:
                pages.append(pytesseract.image_to_string(img, lang="hin"))

        except Exception as e:
            print(f"OCR Failed: {e}")

    print(f"Total Pages Extracted: {len(pages)}")

    # Print first few pages to see structure
    for i in range(min(50, len(pages))):
        print(f"\n--- PAGE {i} ---")
        print(pages[i])
        print("-----------------")


if __name__ == "__main__":
    debug_pdf("data/vedas/Rigved.pdf")
    debug_pdf("data/vedas/Samved.pdf")

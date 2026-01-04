from pdf2image import convert_from_path
import pytesseract
from PIL import Image
from config.settings import TESSERACT_PATH
import os

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def extract_text_from_pdf(pdf_path: str):
    try:
        # Try to use poppler if available
        pages = convert_from_path(
        pdf_path,
        first_page=1,
        last_page=5  # HF-safe default
        )

    except Exception as e:
        # If poppler is not available, raise a clear error
        raise RuntimeError(
            f"PDF processing requires poppler-utils. "
            f"Install it with: sudo apt-get install poppler-utils (Linux) or brew install poppler (macOS). "
            f"Original error: {str(e)}"
        )
    
    all_text = []

    for i, page in enumerate(pages):
        text = pytesseract.image_to_string(page, lang="eng")
        all_text.append(f"\n--- Page {i+1} ---\n{text}")

    return "\n".join(all_text)


if __name__ == "__main__":
    text = extract_text_from_pdf("sample_invoice.pdf")
    print(text)

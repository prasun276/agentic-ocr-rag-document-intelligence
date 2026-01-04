from pdf2image import convert_from_bytes
import pytesseract
from config.settings import TESSERACT_PATH

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def extract_text_from_pdf(pdf_path: str):
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()

    pages = convert_from_bytes(
        pdf_bytes,
        first_page=1,
        last_page=5
    )

    all_text = []
    for i, page in enumerate(pages):
        text = pytesseract.image_to_string(page, lang="eng")
        all_text.append(f"\n--- Page {i+1} ---\n{text}")

    return "\n".join(all_text)

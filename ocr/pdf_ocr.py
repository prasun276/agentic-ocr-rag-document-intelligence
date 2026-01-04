from pdf2image import convert_from_path
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf(pdf_path: str):
    pages = convert_from_path(pdf_path)
    all_text = []

    for i, page in enumerate(pages):
        text = pytesseract.image_to_string(page, lang="eng")
        all_text.append(f"\n--- Page {i+1} ---\n{text}")

    return "\n".join(all_text)


if __name__ == "__main__":
    text = extract_text_from_pdf("sample_invoice.pdf")
    print(text)

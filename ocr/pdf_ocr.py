import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from config.settings import TESSERACT_PATH
import io

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def extract_text_from_pdf(pdf_path: str):
    doc = fitz.open(pdf_path)

    all_text = []

    # HF-safe page limit
    max_pages = min(len(doc), 5)

    for page_num in range(max_pages):
        page = doc.load_page(page_num)

        # Render page to image
        pix = page.get_pixmap(dpi=200)
        img_bytes = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_bytes))

        text = pytesseract.image_to_string(image, lang="eng")
        all_text.append(f"\n--- Page {page_num + 1} ---\n{text}")

    return "\n".join(all_text)

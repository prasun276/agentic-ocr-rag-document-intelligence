from PIL import Image
import pytesseract
from config.settings import TESSERACT_PATH

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def extract_text(image_path:str) -> str:
    """
    Extract text from an image using OCR.
    Args:
        image_path: Path to the image file.
    Returns:
        Text extracted from the image.
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text.strip()


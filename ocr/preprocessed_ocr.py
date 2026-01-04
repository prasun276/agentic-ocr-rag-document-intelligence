import cv2
import pytesseract
from PIL import Image
from config.settings import TESSERACT_PATH

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def preprocess_image(image_path: str):
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Increase contrast (Adaptive Threshold)
    processed = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        10
    )

    return processed

def extract_text_with_preprocessing(image_path: str):
    processed = preprocess_image(image_path)

    # Save temp file (debugging)
    temp_path = "temp_processed.png"
    cv2.imwrite(temp_path, processed)

    image = Image.open(temp_path)
    text = pytesseract.image_to_string(image, lang="eng")

    return text.strip()



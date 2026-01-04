import os
import platform

# Tesseract path configuration for different platforms
if platform.system() == "Windows":
    # Windows: use default installation path or environment variable
    TESSERACT_PATH = os.getenv("TESSERACT_PATH", r"C:\Program Files\Tesseract-OCR\tesseract.exe")
else:
    # Linux/Unix (including Hugging Face Spaces): tesseract is in PATH
    # Use "tesseract" to let the system find it via PATH, or use custom path from env
    TESSERACT_PATH = os.getenv("TESSERACT_PATH", "tesseract")


OCR_CONFIDENCE_THRESHOLD = 60

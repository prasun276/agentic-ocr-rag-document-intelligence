import os
import platform

# Tesseract path configuration for different platforms
if platform.system() == "Windows":
    TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
else:
    # Linux/Unix - use system tesseract
    TESSERACT_PATH = "/usr/bin/tesseract"  # Default Linux path

# Allow override via environment variable
TESSERACT_PATH = os.getenv("TESSERACT_PATH", TESSERACT_PATH)

OCR_CONFIDENCE_THRESHOLD = 60

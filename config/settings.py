import os
import platform
import shutil

# Tesseract path configuration for different platforms
if platform.system() == "Windows":
    # Windows: use default installation path or environment variable
    TESSERACT_PATH = os.getenv("TESSERACT_PATH", r"C:\Program Files\Tesseract-OCR\tesseract.exe")
else:
    # Linux/Unix (including Hugging Face Spaces): try to find tesseract
    # First check environment variable
    TESSERACT_PATH = os.getenv("TESSERACT_PATH")
    
    if not TESSERACT_PATH:
        # Try to find tesseract in common locations
        common_paths = [
            "/usr/bin/tesseract",
            "/usr/local/bin/tesseract",
            "/bin/tesseract"
        ]
        
        for path in common_paths:
            if os.path.exists(path):
                TESSERACT_PATH = path
                break
        
        # If still not found, try using 'which' command
        if not TESSERACT_PATH:
            tesseract_cmd = shutil.which("tesseract")
            if tesseract_cmd:
                TESSERACT_PATH = tesseract_cmd
            else:
                # Fallback: use "tesseract" and let pytesseract handle it
                TESSERACT_PATH = "tesseract"


OCR_CONFIDENCE_THRESHOLD = 60

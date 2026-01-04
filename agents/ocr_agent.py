from ocr.basic_ocr import extract_text
from ocr.pdf_ocr import extract_text_from_pdf

def ocr_agent(state):
    path = state["input_path"]

    if path.lower().endswith(".pdf"):
        text = extract_text_from_pdf(path)
    else:
        text = extract_text(path)
    
    state["raw_text"] = text
    return state
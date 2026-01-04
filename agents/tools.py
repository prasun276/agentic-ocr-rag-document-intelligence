from ocr.preprocessed_ocr import extract_text_with_preprocessing

def preprocessing_tool(input_path: str) -> str:
    """
    OCR preprocessing tool.
    Used only when confidence is low.
    """
    return extract_text_with_preprocessing(input_path)

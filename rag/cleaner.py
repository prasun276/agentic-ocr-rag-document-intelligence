import re

def clean_ocr_text(text: str) -> str:
    """
    Normalize OCR text for RAG ingestion
    """

    # 1. Normalize newlines
    text = re.sub(r"\n{2,}", "\n", text)

    # 2. Remove excessive spaces
    text = re.sub(r"[ \t]{2,}", " ", text)

    # 3. Remove OCR noise characters
    text = text.replace("|", " ")
    text = text.replace("•", " ")

    # 4. Trim
    return text.strip()

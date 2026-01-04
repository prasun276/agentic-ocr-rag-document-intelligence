def chunk_text(text: str, max_chars: int = 800, overlap: int = 100):
    """
    Paragraph-aware chunking for OCR text
    """
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    chunks = []

    current_chunk = ""

    for para in paragraphs:
        # If adding paragraph exceeds size, finalize chunk
        if len(current_chunk) + len(para)  > max_chars:
            chunks.append(current_chunk.strip())

            # overlap from end of previous chunk
            current_chunk = current_chunk[-overlap:] if overlap else ""

        current_chunk += " " + para

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks
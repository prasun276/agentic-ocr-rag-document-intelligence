import pytesseract
from pytesseract import Output
from PIL import Image


def ocr_with_confidence(image_path: str):
    image = Image.open(image_path)
    data = pytesseract.image_to_data(image, output_type=Output.DICT)

    words,confidences = [],[]

    for i in range(len(data["text"])):
        word = data["text"][i].strip()
        conf = int(data["conf"][i])

        if word and conf > 0:
            words.append(word)
            confidences.append(conf)

    avg_confidence = sum(confidences) / len(confidences) if confidences else 0

    return {
        "text": " ".join(words),
        "avg_confidence": avg_confidence,
        "word_count": len(words)
    }

def confidence_decision(result, threshold=60):
    if result["word_count"] == 0:
        return "FAIL_EMPTY"
    if result["avg_confidence"] < threshold:
        return "FAIL_LOW_CONF"
    else:
        return "SUCCESS"
    

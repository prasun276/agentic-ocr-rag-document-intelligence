from ocr.confidence import ocr_with_confidence, confidence_decision
from utils.logger import logger

def confidence_agent(state):
    path = state["input_path"]

    # 🔑 PDF handling
    if path.lower().endswith(".pdf"):
        logger.info("PDF detected — skipping image confidence check")
        state["confidence"] = None
        state["decision"] = "SUCCESS"
        return state

    # Image confidence path
    result = ocr_with_confidence(path)
    decision = confidence_decision(result)

    state["confidence"] = result["avg_confidence"]
    state["decision"] = decision

    logger.info(
        f"OCR confidence={state['confidence']}, decision={state['decision']}"
    )

    return state

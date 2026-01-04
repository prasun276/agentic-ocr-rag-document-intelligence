from agents.tools import preprocessing_tool
from ocr.basic_ocr import extract_text
from utils.logger import logger

def retry_strategy_agent(state):
    """
    Decide how to retry OCR based on retry count.
    """

    retries = state["retry_count"]
    path = state["input_path"]

    # First retry → try preprocessing
    if retries == 0:
        text = preprocessing_tool(path)
        state["raw_text"] = text
        state["retry_reason"] = "used_preprocessing"
        return state

    # Second retry → plain OCR again
    text = extract_text(path)
    state["raw_text"] = text
    state["retry_reason"] = "plain_ocr_retry"

    logger.info(
    f"Retry {state['retry_count']} using {state['retry_reason']}"
    )

    return state

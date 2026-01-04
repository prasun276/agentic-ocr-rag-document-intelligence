MAX_RETRIES = 2

def route_after_confidence(state):
    decision = state["decision"]
    retries = state["retry_count"]

    if decision == "SUCCESS":
        return "retrieval"

    if decision == "LOW_CONFIDENCE" and retries < MAX_RETRIES:
        return "retry_ocr"

    # LOW_CONFIDENCE or FAIL_EMPTY
    return "stop"

def route_after_validation(state):
    if state["decision"] == "ACCEPT":
        return "end"
    return "stop"

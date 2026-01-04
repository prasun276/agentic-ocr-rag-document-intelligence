def stop_agent(state):
    state["answer"] = "OCR confidence too low. Please upload a clearer document."
    return state
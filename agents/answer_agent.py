from rag.qa import answer_question

def answer_agent(state):
    question = state["question"]
    context = state["retrieved_chunks"]

    answer = answer_question(question, context)
    state["answer"] = answer

    return state

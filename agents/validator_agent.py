from openai import OpenAI
from utils.logger import logger

client = OpenAI()

def validator_agent(state):
    answer = state["answer"]
    context = state["retrieved_chunks"]
    path = state["input_path"]

    # 🔑 PDF: skip confidence-based rejection
    if path.lower().endswith(".pdf"):
        logger.info("PDF detected — skipping confidence-based validation")
        state["decision"] = "ACCEPT"
        return state

    # Image-based validation (original behavior)
    validation_prompt = f"""
You are a strict validator.

Answer:
{answer}

Context:
{context}

Check if the answer is fully supported by the context.
Reply with only one word:
- ACCEPT
- REJECT
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": validation_prompt}],
        temperature=0
    )

    verdict = response.choices[0].message.content.strip()
    state["decision"] = verdict

    logger.info(f"Answer validation result={verdict}")

    return state

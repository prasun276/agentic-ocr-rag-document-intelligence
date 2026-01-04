from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def answer_question(question: str, context_chunks: list[str]) -> str:
    context = "\n\n".join(context_chunks)

    prompt = f"""
You are an assistant answering questions strictly using the provided context.
If the answer is not present in the context, say "I don't know".

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()

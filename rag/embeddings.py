from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI

client = OpenAI()

EMBEDDING_MODEL = "text-embedding-3-small"

def  embed_texts(texts: list[str]) -> list[list[float]]:
    embeddings = []

    for text in texts:
        response = client.embeddings.create(
            model = EMBEDDING_MODEL,
            input = text
        )
        embeddings.append(response.data[0].embedding)

    return embeddings

from rag.cleaner import clean_ocr_text
from rag.chunker import chunk_text
from rag.embeddings import embed_texts
from rag.vector_store import VectorStore
from openai import OpenAI

client = OpenAI()

def retrieval_agent(state):
    text = state["raw_text"]

    cleaned = clean_ocr_text(text)
    chunks = chunk_text(cleaned)

    embeddings = embed_texts(chunks)

    store = VectorStore(len(embeddings[0]))
    store.add(embeddings, chunks)

    question = state["question"]

    query_embedding = client.embeddings.create(
        model="text-embedding-3-small",
        input=question
    ).data[0].embedding

    retrieved = store.search(query_embedding, k=2)

    state["chunks"] = chunks
    state["retrieved_chunks"] = retrieved

    return state

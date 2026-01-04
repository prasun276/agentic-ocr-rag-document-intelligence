import streamlit as st
from graph.document_graph import build_graph
import uuid
from pathlib import Path

st.set_page_config(page_title="Agentic OCR-RAG", layout="centered")

st.title("📄 Agentic OCR-RAG Document Intelligence")
st.write("Upload a document and ask questions using an Agentic AI system.")

# Build graph once
graph_app = build_graph()

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

uploaded_file = st.file_uploader(
    "Upload document (Image or PDF)",
    type=["png", "jpg", "jpeg", "pdf"]
)

question = st.text_input(
    "Ask a question",
    value="What is this document about?"
)

if st.button("Ask") and uploaded_file:
    with st.spinner("Agents are reasoning..."):

        file_id = str(uuid.uuid4())
        file_path = UPLOAD_DIR / f"{file_id}_{uploaded_file.name}"

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        result = graph_app.invoke({
            "input_path": str(file_path),
            "question": question,
            "raw_text": None,
            "confidence": None,
            "decision": None,
            "chunks": None,
            "retrieved_chunks": None,
            "answer": None,
            "retry_count": 0,
        })

    st.success("Answer generated")

    st.markdown("### 🤖 Answer")
    st.write(result["answer"])

    st.markdown("### 🔍 Agent Signals")
    st.json({
        "confidence": result["confidence"],
        "decision": result["decision"],
        "retries": result["retry_count"]
    })

import streamlit as st
import os
import traceback
from pathlib import Path

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

try:
    from graph.document_graph import build_graph
    import uuid
except ImportError as e:
    st.error(f"Import error: {e}. Please ensure all dependencies are installed.")
    st.stop()

st.set_page_config(page_title="Agentic OCR-RAG", layout="centered")

st.title("📄 Agentic OCR-RAG Document Intelligence")
st.write("Upload a document and ask questions using an Agentic AI system.")

# Check for OpenAI API key
if not os.getenv("OPENAI_API_KEY"):
    st.warning("⚠️ OPENAI_API_KEY not found. Please set it in the Space settings (Settings → Secrets).")
    st.info("The app requires an OpenAI API key to function. Add it as a secret in your Hugging Face Space settings.")
    st.stop()

# Build graph once (cached)
@st.cache_resource
def get_graph():
    try:
        return build_graph()
    except Exception as e:
        st.error(f"Error building graph: {e}")
        st.stop()

graph_app = get_graph()

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
    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()
    
    with st.spinner("Agents are reasoning..."):
        try:
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
            st.write(result.get("answer", "No answer generated."))

            st.markdown("### 🔍 Agent Signals")
            st.json({
                "confidence": result.get("confidence"),
                "decision": result.get("decision"),
                "retries": result.get("retry_count", 0)
            })
            
            # Clean up uploaded file
            try:
                file_path.unlink()
            except:
                pass
                
        except Exception as e:
            st.error(f"❌ Error processing document: {str(e)}")
            with st.expander("Error Details"):
                st.code(traceback.format_exc())
            
            # Clean up uploaded file on error
            try:
                if 'file_path' in locals():
                    file_path.unlink()
            except:
                pass


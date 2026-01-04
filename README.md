---
title: Agentic OCR-RAG Document Intelligence
emoji: 📄
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
license: mit
---

# 📄 Agentic OCR-RAG Document Intelligence System

An intelligent document processing system that combines OCR (Optical Character Recognition) with RAG (Retrieval-Augmented Generation) using an agentic AI architecture. Upload documents (images or PDFs) and ask questions to get intelligent answers.

## 🚀 Features

- **Multi-format Support**: Process images (PNG, JPG, JPEG) and PDF documents
- **Intelligent OCR**: Automatic text extraction with confidence scoring
- **Agentic Architecture**: Multi-agent system with retry strategies and validation
- **RAG-based Q&A**: Ask questions about your documents and get contextual answers
- **Confidence Scoring**: Built-in confidence assessment for OCR quality
- **Automatic Retry**: Smart retry mechanisms for low-confidence OCR results

## 🏗️ Architecture

The system uses a LangGraph-based agentic workflow:

1. **OCR Agent**: Extracts text from documents
2. **Confidence Agent**: Assesses OCR quality
3. **Retry Strategy Agent**: Applies preprocessing for low-confidence results
4. **Retrieval Agent**: Chunks and embeds text for semantic search
5. **Answer Agent**: Generates answers using RAG
6. **Validator Agent**: Validates answer quality

## 📋 Requirements

### System Dependencies

For Hugging Face Spaces, Tesseract OCR is pre-installed. For local deployment:

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install -y tesseract-ocr poppler-utils
```

**macOS:**
```bash
brew install tesseract poppler
```

**Windows:**
Download and install from:
- Tesseract: https://github.com/UB-Mannheim/tesseract/wiki
- Poppler: https://github.com/oschwartz10612/poppler-windows/releases

### Python Dependencies

All Python dependencies are listed in `requirements.txt` and will be automatically installed.

## 🔧 Setup

### For Hugging Face Spaces

1. **Fork this repository** to your Hugging Face account
2. **Create a new Space** and select "Streamlit" as the SDK
3. **Add your OpenAI API key** as a secret:
   - Go to Settings → Secrets
   - Add a new secret: `OPENAI_API_KEY` with your API key value
4. The Space will automatically build and deploy!

### For Local Development

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd "Agentic OCR-RAG Document Intelligence System"
   ```

2. **Install system dependencies** (see above)

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

5. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

## 📖 Usage

1. **Upload a document**: Click "Upload document" and select an image or PDF file
2. **Enter your question**: Type your question about the document
3. **Click "Ask"**: The system will process your document and generate an answer
4. **View results**: See the answer and agent signals (confidence, decision, retries)

## 🔐 Environment Variables

- `OPENAI_API_KEY` (required): Your OpenAI API key for embeddings and Q&A
- `TESSERACT_PATH` (optional): Custom path to Tesseract executable (auto-detected on Linux)

## 📁 Project Structure

```
.
├── app.py                 # Main Streamlit application
├── agents/                # Agent implementations
│   ├── ocr_agent.py
│   ├── confidence_agent.py
│   ├── retrieval_agent.py
│   ├── answer_agent.py
│   └── ...
├── graph/                 # LangGraph workflow
│   ├── document_graph.py
│   ├── routing.py
│   └── state.py
├── ocr/                   # OCR processing modules
│   ├── basic_ocr.py
│   ├── pdf_ocr.py
│   └── preprocessed_ocr.py
├── rag/                   # RAG components
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── chunker.py
│   └── qa.py
└── requirements.txt       # Python dependencies
```

## 🛠️ Technologies

- **Streamlit**: Web interface
- **LangGraph**: Agent orchestration
- **OpenAI**: Embeddings and Q&A
- **Tesseract OCR**: Text extraction
- **FAISS**: Vector similarity search
- **Pillow & OpenCV**: Image processing

## 📝 License

MIT License

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⚠️ Notes

- The app requires an OpenAI API key to function
- Processing time depends on document size and complexity
- Large PDFs may take longer to process
- The system automatically cleans up uploaded files after processing

from fastapi import APIRouter, UploadFile, File, Form
from api.schemas import ProcessResponse
from graph.document_graph import build_graph
import shutil
import uuid
from pathlib import Path

router = APIRouter()
graph_app = build_graph()

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/process", response_model=ProcessResponse)
def process_document(
    file: UploadFile = File(...),
    question: str = Form(...)
):
    # 1. Save uploaded file
    file_id = str(uuid.uuid4())
    file_path = UPLOAD_DIR / f"{file_id}_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 2. Run agent graph
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

    return ProcessResponse(
        answer=result["answer"],
        confidence=result.get("confidence"),
        decision=result.get("decision"),
        retries=result["retry_count"],
    )

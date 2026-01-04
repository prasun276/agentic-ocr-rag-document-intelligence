from pydantic import BaseModel

class ProcessRequest(BaseModel):
    input_path: str
    question: str

class ProcessResponse(BaseModel):
    answer: str
    confidence: float | None = None
    decision: str | None = None
    retries: int
from typing import TypedDict, List, Optional


class GraphState(TypedDict):
    input_path:str
    question: str
    raw_text: Optional[str]
    confidence: Optional[float]
    decision: Optional[str]
    chunks: Optional[List[str]]
    retrieved_chunks: Optional[List[str]]
    answer: Optional[str]
    retry_count: int
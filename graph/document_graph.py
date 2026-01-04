from langgraph.graph import StateGraph, END
from graph.state import GraphState

from agents.ocr_agent import ocr_agent
from agents.confidence_agent import confidence_agent
from agents.retrieval_agent import retrieval_agent
from agents.answer_agent import answer_agent
from agents.stop_agent import stop_agent
from graph.routing import route_after_confidence, route_after_validation
from agents.retry_ocr_agent import retry_ocr_agent
from agents.validator_agent import validator_agent
from agents.retry_strategy_agent import retry_strategy_agent

def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("ocr", ocr_agent)
    graph.add_node("confidence", confidence_agent)
    graph.add_node("retry_ocr", retry_strategy_agent)
    graph.add_node("retrieval", retrieval_agent)
    graph.add_node("answer", answer_agent)
    graph.add_node("validate", validator_agent)
    graph.add_node("stop", stop_agent)

    graph.set_entry_point("ocr")

    graph.add_edge("ocr", "confidence")

    graph.add_conditional_edges(
        "confidence",
        route_after_confidence,
        {
            "retrieval": "retrieval",
            "retry_ocr": "retry_ocr",
            "stop": "stop",
        }
    )

    graph.add_edge("retry_ocr", "confidence")
    graph.add_edge("retrieval", "answer")
    graph.add_edge("answer", "validate")

    graph.add_conditional_edges(
        "validate",
        route_after_validation,
        {
            "end": END,
            "stop": "stop"
        }
    )

    graph.add_edge("stop", END)

    return graph.compile()
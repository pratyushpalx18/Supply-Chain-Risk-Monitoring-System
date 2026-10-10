from typing import Annotated, TypedDict
import operator

from langgraph.graph import StateGraph, START, END

from agents.news_agent import news_agent
from agents.weather_agent import weather_agent
from agents.supplier_agent import supplier_agent
from agents.risk_manager import risk_manager


class SupplyChainState(TypedDict, total=False):
    supplier_id: str
    location: str
    news: dict
    weather: dict
    supplier: dict
    final: dict
    execution_trace: Annotated[list[dict], operator.add]


def run_news(state):
    result = news_agent(state["location"])
    return {
        "news": result,
        "execution_trace": [{
            "agent": "News & Geopolitical Agent",
            "action": "Called News Search Tool",
            "tool": result.get("tool_name", "News Search Tool"),
            "result": result.get("tool_result", ""),
        }],
    }


def run_weather(state):
    result = weather_agent(state["location"])
    return {
        "weather": result,
        "execution_trace": [{
            "agent": "Weather Risk Agent",
            "action": "Called Weather Tool",
            "tool": result.get("tool_name", "Weather Tool"),
            "result": result.get("tool_result", ""),
        }],
    }


def run_supplier(state):
    result = supplier_agent(state["supplier_id"])
    return {
        "supplier": result,
        "execution_trace": [{
            "agent": "Supplier Risk Agent",
            "action": "Called Supplier CSV Tool",
            "tool": result.get("tool_name", "Supplier CSV Tool"),
            "result": result.get("tool_result", ""),
        }],
    }


def run_risk_manager(state):
    result = risk_manager(state["news"], state["weather"], state["supplier"])
    return {
        "final": result,
        "execution_trace": [{
            "agent": "Risk Manager Agent",
            "action": "Aggregated 3 specialist-agent outputs",
            "tool": "LangGraph Shared State",
            "result": f"Overall risk: {result.get('overall_risk', 'Unknown')}",
        }],
    }


def build_graph():
    graph = StateGraph(SupplyChainState)

    graph.add_node("news_agent", run_news)
    graph.add_node("weather_agent", run_weather)
    graph.add_node("supplier_agent", run_supplier)
    graph.add_node("risk_manager", run_risk_manager)

    # Fan-out: specialist agents run independently.
    graph.add_edge(START, "news_agent")
    graph.add_edge(START, "weather_agent")
    graph.add_edge(START, "supplier_agent")

    # Fan-in: Risk Manager receives all three outputs.
    graph.add_edge("news_agent", "risk_manager")
    graph.add_edge("weather_agent", "risk_manager")
    graph.add_edge("supplier_agent", "risk_manager")
    graph.add_edge("risk_manager", END)

    return graph.compile()


def run_workflow(supplier_id: str, location: str):
    app = build_graph()
    return app.invoke({
        "supplier_id": supplier_id,
        "location": location,
        "execution_trace": [],
    })

from tools.news_tool import search_news

def news_agent(location: str) -> dict:
    """Specialist agent: calls the news search tool and summarizes external events."""
    events = search_news(location)
    severity_order = {"High": 3, "Medium": 2, "Low": 1}
    max_level = max(
        (severity_order.get(e.get("severity", "Low"), 1) for e in events),
        default=1,
    )
    level = {3: "High", 2: "Medium", 1: "Low"}[max_level]

    return {
        "agent": "News & Geopolitical Risk Agent",
        "location": location,
        "events": events,
        "risk_level": level,
        "tool_call": "search_news(location, category='supply chain')",
        "tool_name": "News Search Tool",
        "tool_result": f"{len(events)} event(s) returned",
    }

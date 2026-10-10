from tools.weather_tool import get_weather

def weather_agent(location: str) -> dict:
    """Specialist agent: calls the weather tool and evaluates disruption risk."""
    weather = get_weather(location)

    return {
        "agent": "Weather Risk Agent",
        "location": location,
        "weather": weather,
        "risk_level": weather.get("risk", "Medium"),
        "finding": weather.get("reason", ""),
        "tool_call": "get_weather(location)",
        "tool_name": "Weather Tool",
        "tool_result": f"{weather.get('condition', 'Unknown')} | Risk: {weather.get('risk', 'Medium')}",
    }

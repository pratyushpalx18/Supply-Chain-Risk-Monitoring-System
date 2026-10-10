import os
import requests

def get_weather(location: str) -> dict:
    """Tool: retrieve current weather risk information."""
    api_key = os.getenv("OPENWEATHER_API_KEY")

    # Demo mode makes the project runnable without an external API.
    demo = {
        "Ahmedabad Gujarat": {"condition": "Heavy Rain", "temperature_c": 29, "risk": "High",
                              "reason": "Heavy rainfall may disrupt road transportation."},
        "Mumbai Maharashtra": {"condition": "Cloudy", "temperature_c": 28, "risk": "Medium",
                               "reason": "Poor visibility and rain may cause moderate transport delays."},
        "Surat Gujarat": {"condition": "Heavy Rain", "temperature_c": 28, "risk": "High",
                          "reason": "Heavy rainfall can affect road and warehouse operations."},
        "Pune Maharashtra": {"condition": "Light Rain", "temperature_c": 25, "risk": "Medium",
                             "reason": "Rain may cause localized transportation delays."},
        "Bengaluru Karnataka": {"condition": "Clear", "temperature_c": 24, "risk": "Low",
                                "reason": "No major weather disruption detected in demo mode."},
    }

    if not api_key:
        return demo.get(location, {
            "condition": "Unknown", "temperature_c": None, "risk": "Medium",
            "reason": "No live weather API configured; demonstration assumption used."
        })

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key, "units": "metric"}
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        condition = data["weather"][0]["main"]
        temp = data["main"]["temp"]
        severe = {"Thunderstorm", "Tornado"}
        rain = {"Rain", "Drizzle"}
        if condition in severe:
            risk = "High"
        elif condition in rain:
            risk = "Medium"
        else:
            risk = "Low"
        return {"condition": condition, "temperature_c": temp, "risk": risk,
                "reason": f"Live weather condition: {condition}."}
    except Exception as e:
        return {"condition": "API unavailable", "temperature_c": None, "risk": "Medium",
                "reason": f"Weather API unavailable; fallback used. {e}"}

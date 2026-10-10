import os
import requests

def search_news(location: str, category: str = "supply chain") -> list[dict]:
    """Tool: search external news or use deterministic demo events."""
    api_key = os.getenv("NEWS_API_KEY")

    demo = {
        "Ahmedabad Gujarat": [
            {"title": "Regional transport disruption affects freight movement",
             "category": "transport", "severity": "High",
             "summary": "A simulated transport disruption may delay inbound and outbound shipments."},
            {"title": "Manufacturing supply chain under monitoring",
             "category": "supply_chain", "severity": "Medium",
             "summary": "Companies are advised to maintain contingency inventory."}
        ],
        "Surat Gujarat": [
            {"title": "Heavy rainfall creates logistics disruption risk",
             "category": "weather_transport", "severity": "High",
             "summary": "A simulated weather-related logistics event may affect road movement."}
        ],
        "Mumbai Maharashtra": [
            {"title": "Port congestion risk under observation",
             "category": "logistics", "severity": "Medium",
             "summary": "A simulated congestion event may increase shipment lead times."}
        ]
    }

    if not api_key:
        return demo.get(location, [{
            "title": "No live news configured",
            "category": category,
            "severity": "Low",
            "summary": "Demo mode found no location-specific external event."
        }])

    # NewsAPI-style endpoint. If unavailable, fallback to demo data.
    url = "https://newsapi.org/v2/everything"
    params = {"q": f'"{location}" AND ("supply chain" OR logistics OR strike OR sanction)',
              "apiKey": api_key, "language": "en", "pageSize": 5, "sortBy": "publishedAt"}
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        articles = r.json().get("articles", [])
        results = []
        for a in articles:
            title = a.get("title", "")
            description = a.get("description", "") or ""
            text = (title + " " + description).lower()
            severity = "High" if any(x in text for x in ["war", "strike", "sanction", "closure", "flood"]) else "Medium"
            results.append({"title": title, "category": category,
                            "severity": severity, "summary": description})
        return results or demo.get(location, [])
    except Exception:
        return demo.get(location, [{
            "title": "News API unavailable",
            "category": category,
            "severity": "Medium",
            "summary": "Fallback demonstration event used."
        }])

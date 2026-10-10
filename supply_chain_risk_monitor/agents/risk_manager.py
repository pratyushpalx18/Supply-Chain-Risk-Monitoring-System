def risk_manager(news: dict, weather: dict, supplier: dict) -> dict:
    """Final decision-support agent. Consolidates specialist findings."""
    if "error" in supplier:
        return supplier

    levels = {"Low": 1, "Medium": 2, "High": 3}
    weighted = {
        "news": levels.get(news.get("risk_level", "Low"), 1),
        "weather": levels.get(weather.get("risk_level", "Low"), 1),
        "supplier": levels.get(supplier.get("risk_level", "Low"), 1),
    }

    # Supplier receives the largest weight because it represents direct internal performance.
    score = weighted["supplier"] * 0.5 + weighted["news"] * 0.25 + weighted["weather"] * 0.25
    overall = "High" if score >= 2.4 else "Medium" if score >= 1.5 else "Low"

    actions = []
    if supplier.get("risk_level") == "High":
        actions += ["Contact the supplier immediately and request an updated delivery commitment.",
                    "Evaluate an alternate supplier for critical materials.",
                    "Increase safety-stock coverage if inventory permits."]
    elif supplier.get("risk_level") == "Medium":
        actions.append("Increase supplier monitoring and verify the next shipment milestone.")

    if weather.get("risk_level") == "High":
        actions += ["Check alternate transportation routes and weather-safe dispatch windows."]
    elif weather.get("risk_level") == "Medium":
        actions.append("Track local weather and prepare for possible transportation delays.")

    if news.get("risk_level") == "High":
        actions += ["Validate the external event with an authoritative source.",
                    "Review contingency logistics and supplier alternatives."]
    elif news.get("risk_level") == "Medium":
        actions.append("Continue monitoring external events affecting the supplier region.")

    if not actions:
        actions.append("Continue routine monitoring; no immediate mitigation action is required.")

    return {
        "agent": "Risk Manager Agent",
        "overall_risk": overall,
        "risk_score": round(score / 3 * 100, 1),
        "component_risks": weighted,
        "mitigation_actions": list(dict.fromkeys(actions)),
        "executive_summary": (
            f"{supplier['supplier']['supplier_name']} has an overall {overall.lower()} supply-chain risk. "
            f"The assessment combines supplier performance, external events and weather conditions."
        )
    }

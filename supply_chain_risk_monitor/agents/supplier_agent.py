from tools.supplier_tool import get_supplier_data

def supplier_agent(supplier_id: str) -> dict:
    """Specialist agent: calls the supplier-data tool and evaluates supplier risk."""
    data = get_supplier_data(supplier_id)

    if "error" in data:
        return {
            "agent": "Supplier Risk Agent",
            "error": data["error"],
            "tool_call": f"get_supplier_data('{supplier_id}')",
            "tool_name": "Supplier CSV Tool",
            "tool_result": "Supplier not found",
            "risk_level": "High",
        }

    on_time = float(data["on_time_delivery_pct"])
    quality = float(data["quality_score"])
    delay = float(data["avg_delay_days"])
    coverage = float(data["inventory_coverage_days"])
    financial = data["financial_risk"]

    score = 0
    if on_time < 85:
        score += 30
    elif on_time < 92:
        score += 15
    if quality < 85:
        score += 20
    elif quality < 92:
        score += 10
    if delay > 5:
        score += 25
    elif delay > 2:
        score += 10
    if coverage < 10:
        score += 15
    elif coverage < 15:
        score += 8
    if financial == "High":
        score += 20
    elif financial == "Medium":
        score += 10

    level = "High" if score >= 55 else "Medium" if score >= 25 else "Low"

    return {
        "agent": "Supplier Risk Agent",
        "supplier": data,
        "risk_score": min(score, 100),
        "risk_level": level,
        "findings": [
            f"On-time delivery: {on_time}%",
            f"Quality score: {quality}/100",
            f"Average delay: {delay} days",
            f"Inventory coverage: {coverage} days",
            f"Financial risk: {financial}",
        ],
        "tool_call": f"get_supplier_data('{supplier_id}')",
        "tool_name": "Supplier CSV Tool",
        "tool_result": f"Supplier record retrieved: {data['supplier_name']}",
    }

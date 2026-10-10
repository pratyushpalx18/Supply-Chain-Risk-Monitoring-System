from graph.workflow import run_workflow

def print_report(result):
    print("\n" + "=" * 60)
    print("SUPPLY CHAIN RISK MONITORING SYSTEM")
    print("=" * 60)

    supplier = result["supplier"]["supplier"]
    final = result["final"]

    print(f"\nSupplier: {supplier['supplier_name']} ({supplier['supplier_id']})")
    print(f"Location: {supplier['location']}")
    print(f"Overall Risk: {final['overall_risk']}")
    print(f"Risk Score: {final['risk_score']}/100")

    print("\nAgent Findings")
    print("-" * 60)
    print(f"News Risk: {result['news']['risk_level']}")
    for e in result["news"]["events"]:
        print(f"  - {e['title']} [{e['severity']}]")

    print(f"\nWeather Risk: {result['weather']['risk_level']}")
    print(f"  - {result['weather']['weather']['condition']}")
    print(f"  - {result['weather']['weather']['reason']}")

    print(f"\nSupplier Risk: {result['supplier']['risk_level']}")
    for finding in result["supplier"]["findings"]:
        print(f"  - {finding}")

    print("\nRecommended Mitigation Actions")
    print("-" * 60)
    for i, action in enumerate(final["mitigation_actions"], 1):
        print(f"{i}. {action}")

if __name__ == "__main__":
    result = run_workflow("SUP-001", "Ahmedabad Gujarat")
    print_report(result)

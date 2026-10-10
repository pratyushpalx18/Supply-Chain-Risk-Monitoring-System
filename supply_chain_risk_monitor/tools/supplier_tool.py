import csv
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "suppliers.csv"

def get_supplier_data(supplier_id: str) -> dict:
    """Tool: retrieve supplier performance data from CSV."""
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["supplier_id"].lower() == supplier_id.lower():
                return row
    return {"error": f"Supplier {supplier_id} not found."}

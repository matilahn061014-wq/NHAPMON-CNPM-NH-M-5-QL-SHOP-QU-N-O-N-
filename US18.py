#us18

from datetime import datetime
from collections import defaultdict

sales_data = [
    {
        "product_id": "SP01",
        "product_name": "Áo thun",
        "color": "Đen",
        "size": "M",
        "quantity": 3,
        "date": "12/01/2025",
    },
    {
        "product_id": "SP02",
        "product_name": "Quần jean",
        "color": "Đen",
        "size": "M",
        "quantity": 5,
        "date": "01/01/2025",
    },
    {
        "product_id": "SP03",
        "product_name": "Giày thể thao",
        "color": "white",
        "size": "40",
        "quantity": 7,
        "date": "04/04/2004"
    },
]

def parse_date(date_str: str):
    return datetime.strptime(date_str, "%d/%m/%Y")

def top_selling_products(data, top_n=10, start_date=None, end_date=None, color=None, size=None):
    if start_date:
        start_date = parse_date(start_date)
    if end_date:
        end_date = parse_date(end_date)

    summary = defaultdict(int)

    for row in data:
        sales_date = parse_date(row["date"])

        if start_date and sales_date < start_date:
            continue
        if end_date and sales_date > end_date:
            continue
        if color and row["color"] != color:
            continue
        if size and row["size"] != size:
            continue

        key = (
            row["product_id"],
            row["product_name"],
            row["color"],
            row["size"],
        )
        summary[key] += row["quantity"]

    result = sorted(summary.items(), key=lambda x: x[1], reverse=True)
    return result[:top_n]

if __name__ == "__main__":
    report = top_selling_products(
        sales_data,
        start_date="01/01/2025",
        end_date="31/12/2025"
    )

    for idx, (info, total_qty) in enumerate(report, 1):
        pid, name, color, size = info
        print(f"{idx}. {name} | {pid} | {color} | {size} | {total_qty}")
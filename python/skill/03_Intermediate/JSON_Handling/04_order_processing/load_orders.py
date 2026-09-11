import json

file_path = "json/4/orders.json"

def load_orders():
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not exists, please check")
        return {}

orders_data = load_orders()

orders = orders_data.get("orders", [])

total_orders = len(orders)
paid_orders = 0
unpaid_orders = 0
total_revenue = 0

for order in orders:
    if order.get("paid"):
        paid_orders += 1
        total_revenue += order.get("total", 0)
    else:
        unpaid_orders += 1

print(f"Total orders: {total_orders}")
print(f"Paid orders: {paid_orders}")
print(f"Unpaid orders: {unpaid_orders}")
print(f"Total revenue: {total_revenue}")
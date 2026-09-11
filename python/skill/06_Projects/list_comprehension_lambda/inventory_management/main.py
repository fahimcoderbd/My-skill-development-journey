inventory = [
    {"name": "Keyboard", "stock": 20},
    {"name": "Mouse", "stock": 0},
    {"name": "Monitor", "stock": 5},
    {"name": "Laptop", "stock": 0},
]

#task-1 List all product names.
all_product_names = [product['name'] for product in inventory]

#task-2 Find out-of-stock products.
out_of_stock_products = [product for product in inventory if product['stock'] == 0]

#task-3 Sort by stock quantity.
inventory.sort(key=lambda product: product['stock'])

#task-4 Find the product with the highest stock.
product = max(inventory, key=lambda product: product['stock'])

#testing
print(all_product_names)
print(out_of_stock_products)
print(product)

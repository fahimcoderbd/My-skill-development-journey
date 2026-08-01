cart = [
    {"name": "Mouse", "price": 700},
    {"name": "Keyboard", "price": 2200},
    {"name": "Laptop", "price": 80000},
    {"name": "Monitor", "price": 15000},
]

#task-1
all_product_names = [product['name'] for product in cart]

#task-2
all_product_prices = [product['price'] for product in cart]

#task-3
costly_products = [product for product in cart if product['price'] > 5000]

#task-4
cart.sort(key=lambda product: product['price'])

#task-5
cart.sort(key=lambda product: product['name'])

#testing my codes
print(all_product_names)
print(all_product_prices)
print(costly_products)
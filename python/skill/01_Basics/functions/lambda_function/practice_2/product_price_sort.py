products = [
    {"name": "Laptop", "price": 80000},
    {"name": "Mouse", "price": 700},
    {"name": "Keyboard", "price": 2000},
]

products.sort(key=lambda product: product['price'])
print(products)


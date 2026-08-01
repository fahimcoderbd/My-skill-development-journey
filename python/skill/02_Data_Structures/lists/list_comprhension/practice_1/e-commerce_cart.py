cart = [
    {"name": "Mouse", "price": 500},
    {"name": "Keyboard", "price": 1500},
    {"name": "Monitor", "price": 12000},
]

#amake prices gula ber korte hobe
prices = [item['price'] for item in cart]
expensive = [item['name'] for item in cart if item['price'] > 1000]
print(prices)
print(expensive)
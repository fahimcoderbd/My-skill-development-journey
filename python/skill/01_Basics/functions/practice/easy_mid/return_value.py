def calculate_discount(price):
    if price >= 1000:
        return price - 100
    else:
        return price

print(calculate_discount(1200))
# 1100
    
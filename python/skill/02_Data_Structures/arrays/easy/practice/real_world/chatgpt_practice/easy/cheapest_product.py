def cheapest_product(prices):
    if not prices:
        return 0
    
    min_price = prices[0]

    for price in prices:
        if price < min_price:
            min_price = price
            
    return min_price

print(cheapest_product([450, 120, 700, 300, 250]))
def highest_sale(sales):
    if not sales:
        return 0
    
    if len(sales) < 2:
        return sales
    
    max_sale = sales[0]

    for sale in sales:
        if sale > max_sale:
            max_sale = sale

    return max_sale

sales = [500, 900, 700]
sales2 = [2500]
sales3 = []

print(highest_sale(sales))
print(highest_sale(sales2))
print(highest_sale(sales3))


    
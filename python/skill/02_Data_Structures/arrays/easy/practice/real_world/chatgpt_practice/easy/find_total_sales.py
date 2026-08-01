def total_sales(sales):
    if not sales:
        return None
    
    total_sales = 0

    for sale in sales:
        total_sales += sale

    return (
        f"Total sales is: {total_sales}"
    )

#testing
sales = [1200, 1500, 1800, 1000, 2000, 1700, 1600]
print(total_sales(sales))
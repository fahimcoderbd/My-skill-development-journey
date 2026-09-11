#online shop out of stock items
#14/8/26

def out_of_stock_products(stock:list):
    if not stock: return

    out_of_stock_num = 0
    indexes = []
    for index,stock_num in enumerate(stock):
        if stock_num == 0:
            out_of_stock_num += 1
            indexes.append(index)

    return (
        f"Out of stock: {out_of_stock_num} \n"
        f"Indexes: {indexes}"
    )

print(out_of_stock_products([]))
print(out_of_stock_products([5,0,12,3,0,8,0,15]))
           

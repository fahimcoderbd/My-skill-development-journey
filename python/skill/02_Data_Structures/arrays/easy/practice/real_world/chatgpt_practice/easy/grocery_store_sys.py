'''
🍎 Grocery Store Inventory Checker

একটি ছোট দোকানে কিছু পণ্যের stock আছে:

items = [10, 5, 0, 8, 3, 0, 15]

প্রতিটি সংখ্যা একটি পণ্যের stock quantity বোঝায়।

Tasks
মোট কতটি item stock-এ আছে?
সবচেয়ে বেশি stock কোন quantity?
সবচেয়ে কম stock কোন quantity?
কতগুলো product out of stock? (0)
কতগুলো product low stock? (<= 5)
Average stock কত?
Example Output
Total Stock: 41
Highest Stock: 15
Lowest Stock: 0
Out of Stock Products: 2
Low Stock Products: 4
Average Stock: 5.86
'''

#sollution

""" def average(total_val, length):
    return (total_val / length)

#main function
def main(arr):
    if not arr:
        return None
    
    total_stocks = sum(arr)
    low_stock = 0
    out_of_stock = 0
    
    #counting stocks with logic
    for stock in arr:
        if stock == 0 or stock < 1:
            out_of_stock += 1
        elif stock <= 5:
            low_stock += 1


    #returning outputs
    return (
        f"Showing results for {arr} \n"
        f"Total stock: {total_stocks} \n"
        f"Highest stock: {max(arr)} \n"
        f"Lowest stock: {min(arr)} \n"
        f"Out of stock: {out_of_stock} \n"
        f"Low stock products: {low_stock} \n"
        f"Average stock: {average(total_stocks,len(arr)):.2f} \n"
    ) """


#better sollution
def analyze_inventory(items):
    if not items:
        return None

    total_stock = sum(items)

    out_of_stock = sum(1 for stock in items if stock == 0)
    low_stock = sum(1 for stock in items if stock <= 5)

    return {
        "total_stock": total_stock,
        "highest_stock": max(items),
        "lowest_stock": min(items),
        "out_of_stock": out_of_stock,
        "low_stock": low_stock,
        "average_stock": round(total_stock / len(items), 2)
    }

#testing
items = [10, 5, 0, 8, 3, 0, 15]
print(analyze_inventory(items))
def total_cart(arr):
    if not arr:
        return None
    
    total = sum(arr)
    threshold_cross = total > 1000   # True if total exceeds 1000

    return (
        f"Total shopping: {total}\n"
        f"Free shopping: {threshold_cross}"
    )

prices = [250, 400, 150, 300]
print(total_cart(prices))
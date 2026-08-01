def daily_expense_tracker(arr,k):
    if not arr:
        return None
    
    if k == 0:
        return f"K can't be negative or 0"
    
    first_sum = sum(arr[:k])

    if len(arr[k:]) == k:
       second_sum = sum(arr[k:])
    else:
        return first_sum
    
    if first_sum > second_sum:
        return first_sum
    else:
        return second_sum
    
expenses = [200, 450, 100, 300, 600, 150]
print(daily_expense_tracker(expenses, 3))
    

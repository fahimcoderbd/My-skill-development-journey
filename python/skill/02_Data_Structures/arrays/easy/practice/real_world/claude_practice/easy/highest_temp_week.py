def highest_temp_week(arr):
    if not arr:
        return None
    
    high_temp = max(arr)
    low_temp = min(arr)

    return (
        f"this week's high : {high_temp} \n"
        f"this week's low: {low_temp}"
    )

temps = [30, 28, 35, 32, 29, 31, 33]
print(highest_temp_week(temps))
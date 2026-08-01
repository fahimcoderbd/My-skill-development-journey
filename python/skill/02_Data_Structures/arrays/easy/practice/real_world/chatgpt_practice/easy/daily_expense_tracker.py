'''
🛒 Problem: Daily Expenses Tracker

তোমার ৭ দিনের খরচ একটি array-তে রাখা আছে।

expenses = [120, 250, 100, 300, 150, 200, 180]

Tasks
মোট কত টাকা খরচ হয়েছে বের করো।
সবচেয়ে বেশি খরচ কোন দিনে হয়েছে তা বের করো।
সবচেয়ে কম খরচ কোন দিনে হয়েছে তা বের করো।
গড় (average) খরচ বের করো।
কতদিন 200 টাকার বেশি খরচ হয়েছে তা গণনা করো
।
Example Output
Total Expense: 1300
Maximum Expense: 300
Minimum Expense: 100
Average Expense: 185.71
Days with expense > 200: 2
'''

#calculate average
def get_average(total, length):
    return (total / length) #returning average

#main function
def expense_tracker(arr):
    if not arr:
        return None
    
    #app variables
    total_expense = sum(arr)
    max_expense = max(arr)
    min_expense = min(arr)
    days_with_expense = 0
    average_expense = get_average(total_expense,len(arr))

    #counting days with expense > 200:
    for expense in arr:
        if expense > 200:
            days_with_expense += 1
            
    #returning final values
    return (
        f"Total Expense: {total_expense} \n"
        f"Maximum Expense: {max_expense} \n"
        f"Minimum Expense: {min_expense} \n"
        f"Average Expense: {average_expense :.2f} \n"
        f"Days with expense > 200: {days_with_expense} \n"
    )

expenses = [120, 250, 100, 300, 150, 200, 180]
print(expense_tracker(expenses))


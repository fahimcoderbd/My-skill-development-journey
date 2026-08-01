'''
🛒 Grocery Store Sales Tracker

একটা ছোট grocery store-এর ৭ দিনের sales (টাকায়) একটি array-তে আছে:

sales = [1200, 1800, 1500, 2200, 900, 2500, 1700]

প্রতিটি index = একটি দিন।

তোমার Task

একটি function লিখো:

def sales_report(arr):
    pass

যা বের করবে:

Basic Analysis
Total Sales
Average Sales
Highest Sales Day
Lowest Sales Day
Business Analysis
কতদিন sales average-এর উপরে ছিল
প্রথম কোন দিনে sales 2000 বা তার বেশি হয়েছিল
কতদিন sales 1000 টাকার নিচে ছিল
Expected Output Style
Total Sales: 11800
Average Sales: 1685.71
Highest Sales Day: Day 6
Lowest Sales Day: Day 5
Days Above Average: 3
First Day With 2000+ Sales: Day 4
Days Below 1000 Sales: 1
'''
#my sollution
def get_average(total,length):
    return total / length

def sales_report(arr):
    if not arr:
        return None
    
    total_sales = sum(arr)
    average_sales = get_average(total_sales, len(arr))
    highest_sales_day = arr.index(max(arr)) + 1
    lowest_sales_day = arr.index(min(arr)) + 1
    days_above_avg = 0
    first_day_200plus = 0
    sales_below_1000 = 0

    #searching and sorting logic
    for i,sale in enumerate(arr,start=1):
          
        if sale > average_sales:
            days_above_avg += 1

        if sale >= 2000 and first_day_200plus == 0:
           first_day_200plus = i

        if sale < 1000:
            sales_below_1000 += 1

    #returning output
    return (
        f"Total Sales: {total_sales} \n"
        f"Average Sales: {average_sales:.2f} \n"
        f"Highest Sales Day: Day {highest_sales_day} \n"
        f"Lowest Sales Day: Day {lowest_sales_day} \n"
        f"Days Above Average: {days_above_avg} \n"
        f"First Day With 2000+ Sales: {first_day_200plus} \n"
        f"Days Below 1000 Sales: {sales_below_1000} \n"
    )

sales = [1200, 1800, 1500, 2200, 900, 2500, 1700]
print(sales_report(sales))

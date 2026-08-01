""" 📱 Mobile Shop Sales Tracker

একটি মোবাইল দোকান ৭ দিনে কতগুলো ফোন বিক্রি করেছে তার ডাটা একটি array-তে রাখা আছে।

sales = [12, 8, 15, 20, 10, 18, 14]

এখানে:

Day 1 → 12 phones
Day 2 → 8 phones
Day 3 → 15 phones
...
Task

একটি function লিখো:

def sales_tracker(arr):
    pass

যা বের করবে:

Total phones sold
Average sales per day
Highest sales day (Day Number)
Lowest sales day (Day Number)
কতদিন 15 বা তার বেশি phone বিক্রি হয়েছে
প্রথম কোন দিনে sales 20 হয়েছিল (যদি না থাকে "Not Found")
Expected Output
Total Sales: 97
Average Sales: 13.86
Highest Sales Day: Day 4
Lowest Sales Day: Day 2
Days With 15+ Sales: 3
First Day With 20 Sales: Day 4
Bonus Challenge 🚀

আরও বের করার চেষ্টা করো:

Consecutive 2 days-এর সর্বোচ্চ combined sales
Sales array sorted করলে কেমন হয়
কোন দিন average-এর উপরে sales হয়েছে """

def get_average(total,length):
    return total / length

def sales_tracker(arr):
    if not arr:
        return None
    
    #data variables
    total_phones_sold = sum(arr)
    highest_sales_day = arr.index(max(arr)) + 1
    lowest_sales_day = arr.index(min(arr)) + 1
    total_sales_day_more_than_15 = 0
    first_sales_day_with_20 = "Not found"

    #sorting and searching
    for sales_data in arr:
        if sales_data >= 15:
            total_sales_day_more_than_15 += 1
        if sales_data == 20:
            first_sales_day_with_20 = arr.index(sales_data) + 1
        
    #finally returning output
    return (
         f"Total Sales: {total_phones_sold} \n"
         f"Average Sales: {get_average(total_phones_sold, len(arr)):.2f} \n"
         f"Highest Sales Day: Day {highest_sales_day} \n"
         f"Lowest Sales Day: Day {lowest_sales_day} \n"
         f"Days With 15+ Sales: {total_sales_day_more_than_15} \n"
         f"First Day With 20 Sales: Day {first_sales_day_with_20}"
    )

#testing code
sales = [12, 8, 15, 20, 10, 18, 14]
print(sales_tracker(sales))
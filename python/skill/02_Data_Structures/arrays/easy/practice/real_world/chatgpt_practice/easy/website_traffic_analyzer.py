'''
🌐 Website Traffic Analyzer

তুমি একটা SaaS product বানিয়েছো। গত ৭ দিনে কতজন visitor এসেছে তা array-তে আছে:

visitors = [120, 150, 90, 200, 180, 220, 160]

প্রতিটি index = একটি দিন।

Day 1 → 120 visitors
Day 2 → 150 visitors
...
তোমার Task

একটি function লিখো:

def traffic_analyzer(arr):
    pass

যা বের করবে:

Basic Analysis
Total visitors
Average visitors per day
Highest traffic day (Day Number)
Lowest traffic day (Day Number)
Business Analysis
কতদিন average-এর চেয়ে বেশি visitor এসেছে
প্রথম কোন দিনে 200+ visitor এসেছে
Highest growth day

উদাহরণ:

Day 3 = 90
Day 4 = 200

Growth = +110

যে দিনে আগের দিনের তুলনায় সবচেয়ে বেশি visitor বেড়েছে, সেই Day Number বের করতে হবে।

Example Output
Total Visitors: 1120
Average Visitors: 160.0
Highest Traffic Day: Day 6
Lowest Traffic Day: Day 3
Days Above Average: 2
First Day With 200+ Visitors: Day 4
Highest Growth Day: Day 4
'''

def get_average(total,length):
    return total / length

def traffic_analyzer(arr):
    if not arr:
        return None
    
    #basic
    total_visitors = sum(arr)
    average = get_average(total_visitors, len(arr))
    highest_traffic_day = arr.index(max(arr)) + 1
    lowest_traffic_day = arr.index(min(arr)) + 1
    #business
    days_above_average = 0
    first_day_with_200plus = None
    
    if arr[1] > arr[0]:
        highest_growth = arr[1] - arr[0]
    else:
        highest_growth = arr[0] - arr[1]

    highest_growth_day = None

    if arr[0] > average:
        days_above_average += 1

    for i in range(1,len(arr)):
        #calculating days above average
        cal_average = average
        if arr[i] > cal_average:
            days_above_average += 1
        
        #calculating first day > 200
        if arr[i] >= 200 and first_day_with_200plus is None :
            first_day_with_200plus = i+1
        
        #calculate today's visitor - previous day's visitor
        calculated_growth = (arr[i] - arr[i-1])
        
        #calculating highest growth day
        if calculated_growth > highest_growth:
            highest_growth = (arr[i] - arr[i-1])
            highest_growth_day = i+1
    
    #returning output
    return (
        f"Total Visitors: {total_visitors} \n"
        f"Average Visitors: {average:.1f} \n"
        f"Highest Traffic Day: Day {highest_traffic_day} \n"
        f"Lowest Traffic Day: Day {lowest_traffic_day} \n"
        f"Days Above Average: {days_above_average} \n"
        f"First Day With 200+ Visitors: Day {first_day_with_200plus} \n"
        f"Highest Growth Day: Day {highest_growth_day} \n"
    )

visitors = [120, 150, 90, 200, 180, 220, 160]
print(traffic_analyzer(visitors))




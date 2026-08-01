'''
Mobile Battery Usage Analysis
'''

def get_average(total, length):
    return total / length


def battery_analyzer(arr):
    if not arr:
        return None

    # Basic Analysis
    total_usage = sum(arr)
    avg_usage = get_average(total_usage, len(arr))
    highest_battery_day = arr.index(max(arr)) + 1
    lowest_battery_day = arr.index(min(arr)) + 1

    # App Analytics
    more_than_avg_day_count = 0
    first_day_more_than_25 = None
    battery_usage_less_than_15 = 0

    # Smart Analysis
    high_increase = arr[1] - arr[0]
    highest_increase_day = 2

    # Analytics Loop
    for i, usage in enumerate(arr, start=1):

        if usage > avg_usage:
            more_than_avg_day_count += 1

        if usage >= 25 and first_day_more_than_25 is None:
            first_day_more_than_25 = i

        if usage < 15:
            battery_usage_less_than_15 += 1

    # Increase Calculation
    for i in range(1, len(arr)):

        calculated_increase = arr[i] - arr[i - 1]

        if calculated_increase > high_increase:
            high_increase = calculated_increase
            highest_increase_day = i + 1

    return (
        f"Total Battery Used: {total_usage}%\n"
        f"Average Usage: {avg_usage:.2f}%\n"
        f"Highest Usage Day: Day {highest_battery_day}\n"
        f"Lowest Usage Day: Day {lowest_battery_day}\n"
        f"Days Above Average: {more_than_avg_day_count}\n"
        f"First Day With 25%+ Usage: Day {first_day_more_than_25}\n"
        f"Days Below 15% Usage: {battery_usage_less_than_15}\n"
        f"Highest Increase Day: Day {highest_increase_day}"
    )


# Demo
battery_usage = [12, 18, 25, 15, 30, 22, 10]
print(battery_analyzer(battery_usage))
# Your code structure should look something like this:

import json

def process_data(*args, **kwargs):
    try:
        # 1. Flatten args using list comprehension
        flattened_args = [item for sublist in args for item in sublist]
        # 2. Calculate stats (sum, max, etc.)
        total_revenue = sum(flattened_args)
        max_revenue = max(flattened_args)
        # 3. Calculate total overhead from kwargs
        total_overhead = sum(kwargs.get(key, 0) for key in kwargs)
        # 4. Use a lambda to calculate net profit
        net_profit = lambda revenue, overhead: revenue - overhead
        # 5. Save dict to JSON
        result = {
            "total_revenue": total_revenue,
            "max_revenue": max_revenue,
            "total_overhead": total_overhead,
            "net_profit": net_profit(total_revenue, total_overhead)
        }
        with open("output.json", "w") as f:
            json.dump(result, f)
    except Exception as e:
        print(f"An error occurred: {e}")

# Test the function
process_data([500, 200, 500], [1000, 50], Marketing={"ads": 200})
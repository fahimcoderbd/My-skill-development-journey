""" numbers = [3, 7, 10, 15, 20, 25]

def find_even(nums):
    evens = [num for num in nums if num % 2 == 0]
    return evens

evens = find_even(numbers)
print(evens) """


""" def leaderboard(scores):
    highest_score = max(scores)
    lowest_score = min(scores)
    average_score = sum(scores) / len(scores)

    unique_scores = list(set(scores))
    
    print(f"Highest score: {highest_score}")
    print(f"lowest score: {lowest_score}")
    print(f"Average score: {average_score}")
    print(f"unique scores: {unique_scores}")

scores = [10, 20, 20, 50, 60]
leaderboard(scores) """
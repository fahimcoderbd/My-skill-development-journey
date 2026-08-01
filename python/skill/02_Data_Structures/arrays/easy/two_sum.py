#two sum problem
def two_sum(arr, target):
    seen = {}  # { number: index }

    for i, num in enumerate(arr):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]  # found!

        seen[num] = i  # না পেলে save করো

    return []  # no solution

#test cases
arr1 = [2, 7, 11, 15]
target1 = 9
arr2 = [3, 2, 4]
target2 = 6

print(two_sum(arr1, target1))
print(two_sum(arr2, target2))
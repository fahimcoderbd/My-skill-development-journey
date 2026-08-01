#Binary search last ocurance problem
#arr = [1,2,2,2,5], target = 2, output: 3 , arr[3] = 2
#I have to find the last ocuurance last index of the target


def binary_search(arr, target):
    if not arr:
        return None
    
    left = 0
    right = len(arr) - 1
    last_occurance = None

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            last_occurance = mid
            left = mid + 1
            
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1

    if last_occurance is not None:
       return last_occurance
    return -1

# Test cases
print(binary_search([1, 2, 2, 2, 3, 4], 2))  # Expected: 3
print(binary_search([1, 1, 1, 1, 1], 1))  # Expected: 4
print(binary_search([1, 2, 3, 4, 5], 3))  # Expected: 2
print(binary_search([1, 2, 3, 4, 5], 6))  # Expected: -1
print(binary_search([2, 2, 2, 2, 2], 2))  # Expected: 4
print(binary_search([1, 2, 3, 4, 5], 1))  # Expected: 0
print(binary_search([1, 2, 3, 4, 5], 5))  # Expected: 4
print(binary_search([1, 1, 2, 2, 2, 3, 3], 3))  # Expected: 6
print(binary_search([10], 10))  # Expected: 0
print(binary_search([10], 5))  # Expected: -1




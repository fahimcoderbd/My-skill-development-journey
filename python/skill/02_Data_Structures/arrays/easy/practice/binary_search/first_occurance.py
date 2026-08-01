#Binary search first occurance problem
#exmaple arr
#arr = [1,2,2,2,3,4,5]
#target = 2

def binary_search(arr, target):
    if not arr:
        return None
    
    #saving first_occurane
    first_occurance = None

    #logic for searching
    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            first_occurance = mid
            right = mid - 1
        
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1

    if first_occurance is not None:
        return first_occurance
    return -1

# Test cases
print(binary_search([1, 2, 2, 2, 3, 4], 2))  # Expected: 1
print(binary_search([1, 1, 1, 1, 1], 1))  # Expected: 0
print(binary_search([1, 2, 3, 4, 5], 3))  # Expected: 2
print(binary_search([1, 2, 3, 4, 5], 6))  # Expected: -1
print(binary_search([2, 2, 2, 2, 2], 2))  # Expected: 0
print(binary_search([1, 2, 3, 4, 5], 1))  # Expected: 0
print(binary_search([1, 2, 3, 4, 5], 5))  # Expected: 4
print(binary_search([1, 1, 2, 2, 2, 3, 3], 3))  # Expected: 5
print(binary_search([10], 10))  # Expected: 0
print(binary_search([10], 5))  # Expected: -1



        

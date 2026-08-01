#Check if array is palindrome— two pointer
from copy import deepcopy

def check_palindrome(arr):
    if not arr:
        return None
    
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:  # মিলল না → False
            return False
        left += 1
        right -= 1

    return True  # সব মিলেছে → True

#test cases
arr1 = [1, 2, 1]        # True  — symmetric
arr2 = [1, 2, 3]        # False — not symmetric
arr3 = [1]              # True  — single element
arr4 = []               # True/None — empty (তুই decide করবি)
arr9  = [-1, 2, -1]     # True  — negative numbers
arr10 = [1, 1]          # True  — two same elements
arr11 = [1, 2]          # False — two different elements

print(check_palindrome(arr1))
print(check_palindrome(arr2))
print(check_palindrome(arr3))
print(check_palindrome(arr4))
print(check_palindrome(arr9))
print(check_palindrome(arr10))
print(check_palindrome(arr11))

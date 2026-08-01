#Checking arr is palindrome or not

#exmaple arr [1,2,1]

def is_palindrome(arr):
    if not arr:
        return True  # Issue 1: Empty array should return True (it's technically a palindrome)

    # Issue 2: Logic was incomplete - missing increment/decrement of pointers and comparison logic
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:  # Issue 3: Should check if elements are NOT equal (mismatch)
            return False
        left += 1  # Issue 4: Must increment left pointer
        right -= 1  # Issue 5: Must decrement right pointer
    return True

#test cases
arr1 = [1, 2, 1]        # True  — symmetric
arr2 = [1, 2, 3]        # False — not symmetric
arr3 = [1]              # True  — single element
arr4 = []               # True/None — empty (তুই decide করবি)
arr9  = [-1, 2, -1]     # True  — negative numbers
arr10 = [1, 1]          # True  — two same elements
arr11 = [1, 2]          # False — two different elements
arr12 = [1,2,1]


print(is_palindrome(arr1))
print(is_palindrome(arr2))
print(is_palindrome(arr3))
print(is_palindrome(arr4))
print(is_palindrome(arr9))
print(is_palindrome(arr10))
print(is_palindrome(arr11))

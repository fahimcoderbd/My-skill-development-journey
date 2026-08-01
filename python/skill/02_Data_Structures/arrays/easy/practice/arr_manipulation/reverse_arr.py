#arr = [1,2,3,4,5]

def reverse_arr(arr):
    if not arr:
        return []
    
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # swapping logic for reversion
        arr[left], arr[right] = arr[right], arr[left]
        
        left += 1
        right -= 1

    return arr

#testing
arr1 = []
arr2 = [1,1,1,1]
arr3 = [1]
arr4 = [1,2,3,4]
arr5 = [2,4,3,7]

print(reverse_arr(arr1))
print(reverse_arr(arr2))
print(reverse_arr(arr3))
print(reverse_arr(arr4))
print(reverse_arr(arr5))
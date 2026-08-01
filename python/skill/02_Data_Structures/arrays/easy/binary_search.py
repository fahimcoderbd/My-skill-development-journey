#test cases
arr1 = [1, 3, 5, 7, 9, 11, 15]
target1 = 9

def binary_search(arr, target):
    left_side = 0
    right_side = len(arr)
    
    while left_side <= right_side:

        mid = (left_side + right_side) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] <= right_side:
            left_side = mid + 1
        else:
            right_side = mid - 1

    return -1
    

print(binary_search(arr1,target1))

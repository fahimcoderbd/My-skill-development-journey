def move_zeroes_to_end(arr):

    #handling edge cases
    if not arr:
        return None
    if len(arr) < 2:
        return arr

    wp = 0 #write pointer copy positions of zero

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[wp] = arr[wp], arr[i]
            wp += 1

    return arr

#testing
arr1 = [0, 1, 0, 3, 12]
arr2 = [0, 0, 1]
arr3 = [1, 2, 3]
arr4 = [0]

print(move_zeroes_to_end(arr1))
print(move_zeroes_to_end(arr2))
print(move_zeroes_to_end(arr3))
print(move_zeroes_to_end(arr4))
        
arr1 = [1,2,3,4,5]

def right_arr_rotate(arr):
    if not arr:
        return None
    
    last = arr[-1]

    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i - 1]
        print(f"Updated {arr[i]} to {arr[i-1]}")

    return arr

print(right_arr_rotate(arr1))
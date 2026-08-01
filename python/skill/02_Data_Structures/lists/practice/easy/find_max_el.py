def maximum_el(arr):
    if not arr:
        return None
    
    max_num = arr[0]

    for el in arr:
        if el > max_num:
            max_num = el
    return max_num

arr = [5, 2, 9, 1, 7]
print(maximum_el(arr))
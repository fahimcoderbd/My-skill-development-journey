def second_largest_num(arr):
    if not arr:
        return None
    
    if len(arr) < 2:
        return None

    first_largest = arr[0]
    second_largest = arr[1]

    if first_largest < second_largest:
        first_largest, second_largest = second_largest, first_largest

    for i in range(2, len(arr)):
        if arr[i] > first_largest:
            second_largest = first_largest
            first_largest = arr[i]

        elif second_largest < arr[i] < first_largest:
            second_largest = arr[i]

    return second_largest


arr = [10, 5, 20, 8, 15]
print(second_largest_num(arr))
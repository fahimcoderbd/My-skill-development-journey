def second_largest_element(arr):
    if len(arr) < 2:
        return -1

    largest = float('-inf')
    second = float('-inf')

    for el in arr:
        if el > largest:
            second = largest
            largest = el
        elif el > second and el != largest:
            second = el

    return second if second != float('-inf') else -1
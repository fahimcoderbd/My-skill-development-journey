
def second_largest_num(arr):
    if len(arr) < 2:
        return None

    first = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second


arr = [5, 10, 15, 20]
print(second_largest_num(arr))
#Array-এর সবচেয়ে বড় সংখ্যা খুঁজে বের করো

#sollution
def max_of_arr(arr):
    if not arr:
        return None
    
    max_num = arr[0]

    for el in arr:
        if el > max_num:
            max_num = el
    
    return max_num

#test cases
arr1 = [3, 7, 1, 9, 4, 2]
arr2 = [5, 5, 5]

print(max_of_arr(arr1))
print(max_of_arr(arr2))
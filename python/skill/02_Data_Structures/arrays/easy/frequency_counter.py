#frequency counter

def frquency_counter(arr):
    if not arr:
        return f"{arr} is empty,  must have elements!"
    
    arr_freq = {}

    for el in arr:
        arr_freq[el] = arr_freq.get(el, 0) + 1
    return arr_freq

#testing
#test cases
arr1 = []
arr2 = [1,1,2,3,3,4,5]
arr3 = [1]
arr4 = [1,2,3,4,5]
arr5 = [-1, -1, 2]
arr6 = [1, "a", 1, "a"]
arr7 = [3, 3, 3, 3]

print(frquency_counter(arr1))
print(frquency_counter(arr2))
print(frquency_counter(arr3))
print(frquency_counter(arr4))
print(frquency_counter(arr5))
print(frquency_counter(arr6))
print(frquency_counter(arr7))

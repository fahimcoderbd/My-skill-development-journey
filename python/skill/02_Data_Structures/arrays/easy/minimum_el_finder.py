#min element finder

def minimum_el_finder(arr):

    if not arr:
        return f"Your array is empty,need elements"
    
    min_el = arr[0]
    
    for el in arr:
        if el < min_el:
            min_el = el

    return min_el

#test cases
arr1 = [5,5,5] #
arr2 = [1,2,3] #1
arr3 = [5,4,6] #4
arr4 = []

print(minimum_el_finder(arr1))
print(minimum_el_finder(arr2))
print(minimum_el_finder(arr3))
print(minimum_el_finder(arr4))
#counting element in array using binary search
#example arr = [1,2,3,3,4,5]

def first_occurance(arr,target):
    if not arr:
        return None
    
    left = 0
    right = len(arr) - 1
    first_occur = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
           first_occur = mid
           right = mid - 1

        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return first_occur

def last_occurance(arr,target):
    if not arr:
        return None
    
    left = 0
    right = len(arr) - 1
    last_occur = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
           last_occur = mid
           left = mid + 1

        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return last_occur

def frequency_counter(first, last):
    return (last - first) + 1 #this will return the frequency of an arr

#test cases
arr1 = [1,2,3,3,4,5]
target = 3

first_index = first_occurance(arr1, target)
last_index = last_occurance(arr1 , target)

print(frequency_counter(first_index,last_index))
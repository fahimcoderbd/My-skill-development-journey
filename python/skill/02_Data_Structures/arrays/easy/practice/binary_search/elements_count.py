#binary search target frequency in sorted array
#input arr = [1,2,3,4,5,6,6] , target = 6, output = 2(1+1)

""" #my sollution work for only 1 target
def frequency_counter(arr,target):
    if not arr:
        return None
    
    freq = {} #{6:2}

    #running binary search
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:

            if arr[mid] in freq:
                freq[arr[mid]] += 1
            else:
                freq[arr[mid]] = 1

        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if freq:
        return freq
    else:
        return -1

arr = [1,2,3,4,5,6,6]
target = 6
print(frequency_counter(arr,target))
print(frequency_counter([1] , 4))
print(frequency_counter([1] , 1)) """

""" Reverse an array— two pointer """

def reverse_arr_1(arr):
    if not arr:
        return None
    
    left = 0
    right = len(arr) - 1

    while left < right:
        #swap
        arr[left] , arr[right] = arr[right], arr[left]
        
        left += 1
        right -= 1

    return arr

def reverse_arr_best(arr):
    if not arr:
        return None
    return arr[::-1]
    

#test cases
arr1 =  [1, 2, 3, 4, 5]
print(reverse_arr_1(arr1))
print(reverse_arr_best(arr1))
#sum and average of array
#sollution

def sum_average_of_arr(arr):
    if not arr:
        return None
    
    sum_of_arr = 0
    for el in arr:
        sum_of_arr += el

    #average algorithm
    avg_of_arr = sum_of_arr / len(arr)

    return sum_of_arr,avg_of_arr

#test cases
arr1 = [5,5,5] #
arr2 = [1,2,3] #1
arr3 = [5,4,6] #4

print(sum_average_of_arr(arr1))
print(sum_average_of_arr(arr2))
print(sum_average_of_arr(arr3))
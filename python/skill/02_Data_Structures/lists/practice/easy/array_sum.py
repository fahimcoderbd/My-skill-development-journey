def array_sum(arr):
    sum = 0
    #looping the array
    for nums in arr:
        #adding all numbers with sum 0+num+num ....
        sum += nums

    #returning the final sum
    return f"The sum of array is {sum}"

#testing
nums =  [1, 3, 5]
print(array_sum(nums))
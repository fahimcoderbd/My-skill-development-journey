def even_number_array(arr):
    #handling empty array
    if not arr:
        return 
    for numbers in arr:
        if numbers % 2 == 0:
            print(f"Even numbers: {numbers}")
        
    else:
            return "Even not found"
        
#testing
arr1 = [1, 10, 20, 25, 40]
test1 = even_number_array(arr1)

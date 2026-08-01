def even_number_extractor(number_list):
    store_evens = []
    #checking empty arry
    if not number_list:
        return
    for number in number_list:
        if number % 2 == 0:
           store_evens.append(number)
    return store_evens

arr = [1, 2, 3, 4, 5, 6]
numbers = even_number_extractor(arr)
print(numbers)
    
    
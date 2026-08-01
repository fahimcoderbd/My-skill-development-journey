'''
একটা list দেওয়া থাকবে যেখানে প্রতিটা element = ঐ দিনের মোট বিক্রয় (টাকায়)। Maximum sales যেদিন হয়েছে সেই দিনের index (1-based) এবং amount return করো।

sales = [1200, 3500, 2800, 4100, 900]

Output: Day 4, Sales: 4100
'''

""" def maximum_sales_calculator(arr):
    if not arr:
        return None
    
    max_sales = max(arr) #getting maximum sales
    
    for i,el in enumerate(arr,start=1):
        if el == max_sales: #checking el == maximim sales if yes, then index
            index = i

    return f"Day: {index}, Sales: {max_sales}" """

#improved version
def maximum_sales_calculator(arr):
    if not arr:
        return None
    
    max_sales = arr[0]
    max_index = 1

    for i, el in enumerate(arr, start=1):
        if el > max_sales:
            max_sales = el
            max_index = i

    return f"Day: {max_index}, Sales: {max_sales}"

#test cases
sales = [1200, 3500, 2800, 4100, 900]
print(maximum_sales_calculator(sales))




        
    


#built in funcs

def print_data(data):
    print(data)

def get_len(data):
    print(f"the len of {data} is {len(data)}")

def get_type(data):
    print(f"the type of {data} is {type(data)}")

def sort_data(data, reverse=False):
    data_sorted = sorted(data, reverse=reverse)
    print(f"the sorted data is {data_sorted}")

def abs_value(num):
    print(f"the absolute value of {num} is {abs(num)}")
    
#example usage

arry = [1,2,3]
un_sorted = [3,2,1]
num = -10.0

print_data("hellow world")
get_len(arry) #get len of element
get_type(arry) #get type of element
sort_data(un_sorted, reverse=False) #sort data
abs_value(num) #get absolute value
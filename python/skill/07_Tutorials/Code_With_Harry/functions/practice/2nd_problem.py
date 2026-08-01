from functools import reduce

""" prices = [100, 200, 300, 400]

apply_discount = list(map(lambda x: x * 0.9, prices)) #compute discount
print(f"Updated princes: {apply_discount}") """

#2nd problem
""" users = [
    {"name": "Fahim", "active": True},
    {"name": "Rahim", "active": False},
    {"name": "Karim", "active": True}
]

active_users = list(filter(lambda x: x['active'], users))
print(active_users)
 """

#3rd problem

""" cart = [150, 200, 50]

total_cart_value = reduce(lambda x, y: x  + y, cart)
print(f"Total cart value is : {total_cart_value}") """

#4rth problem
""" numbers = [1, 2, 3, 4, 5, 6]

find_even_numbers = list(filter(lambda x: x % 2 == 0 ,numbers))
result = list(map(lambda x: x ** 2, find_even_numbers))

print(f"Final result: {result}") """


#5th problem
""" words = ["ai", "python", "code", "developer"]

result = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(f"Longest word: {result}") """

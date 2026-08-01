'''
Problem 5 (Real World)

একটি shopping cart আছে:

cart = ["Keyboard", "Mouse", "Monitor"]
"Laptop"-কে index 1-এ insert করো।
তারপর পুরো list-টি alphabetically sort করো।
তারপর list-টি reverse করো।
শেষে print করো।
'''

cart = ["Keyboard", "Mouse", "Monitor"]
cart.insert(1, "Laptop")
cart.sort()
cart.reverse()
print(cart)
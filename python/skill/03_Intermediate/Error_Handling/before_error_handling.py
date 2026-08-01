#before error handling
#if i input string,this will crash with ValueError
""" num = int(input("Enter a number: "))
print(num + 10) """

#after error handling
try:
    num2 = int(input("Enter a number: "))
    print(num2 + 10)
except ValueError:
    print("\033[91m")
    print("please enter an integer")
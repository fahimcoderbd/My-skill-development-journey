#login checker decorator

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")

@my_decorator
def say_hello():
    print("Hellow, user!")

say_hello()
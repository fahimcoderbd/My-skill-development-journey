#decorator
def decorator(func):
    def wrapper():
        print("start")
        func()
        print("End")
    return wrapper

#main function
@decorator
def hello():
    print("hellow from main function")

hello()
#decorator
def decorator(func):
    def wrapper():
        print(f"Running function {func.__name__}")
        func()
    return wrapper

#main function
@decorator
def hello():
    print("hellow from main function")

hello()
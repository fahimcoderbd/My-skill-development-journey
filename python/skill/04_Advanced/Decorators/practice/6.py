def decorator(func):
    counter = 0
    
    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1
        result = func(*args, **kwargs)
        print(f"Called {counter} times")
        return result
    
    return wrapper

@decorator
def hello():
    print("hello")

hello()
hello()


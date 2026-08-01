def function_tracker(func):
    count = 0
    def wrapper():
        while func():
            count += 1
        print(count)
    return wrapper

@function_tracker
def hello():
    print("hello")

hello()
hello()
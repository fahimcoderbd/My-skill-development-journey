from functools import wraps

#excecution logger

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with args: {args, kwargs}")
        final_result = func(*args, **kwargs)
        print(f"Function result: {final_result}")
        return final_result
    return wrapper

@log_execution
def add_numbers(a, b):
    return a + b

add_numbers(5,10)

        

    
from functools import wraps

def ensure_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for num in args:
            if num < 0:
                print("Error: Negative inputs are not allowed!")
                return None
        run_function = func(*args, **kwargs)
        return run_function
    return wrapper

@ensure_positive
def multiply(a, b):
    return a * b

print(multiply(5, 4))   # Output hobe: 20
print(multiply(5, -2))  # Output hobe: Error message ar None
from functools import wraps
import time

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
         start_time = time.time()
         run_function = func(*args, **kwargs)
         end_time = time.time()

         time_taken = end_time - start_time
         print(f"Function {func.__name__} taken {time_taken} seconds")
         return run_function
    return wrapper

@time_it
def calculate(a, b):
    return a+b

calculate(5,4)

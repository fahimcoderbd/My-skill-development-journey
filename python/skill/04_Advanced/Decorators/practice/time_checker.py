import time

def time_checker(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        time_taken = (end - start)
        print(f"Total time taken: {time_taken:.4f} sec")
        return result
    return wrapper

@time_checker
def hello():
     for i in range(1, 40000):
        print("hello")

hello()
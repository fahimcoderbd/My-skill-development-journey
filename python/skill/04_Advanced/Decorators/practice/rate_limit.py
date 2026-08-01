import time

def rate_limit(seconds):
    def decorator(func):
        last_called = 0
        
        def wrapper(*args, **kwargs):
            nonlocal last_called
            current_time = time.time()
            
            if current_time - last_called < seconds:
                print(f"Wait {seconds} seconds!")
                return
            
            last_called = current_time
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

@rate_limit(5)
def api_call():
    print("API called")
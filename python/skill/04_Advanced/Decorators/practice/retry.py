def retry(attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Retry {i+1}/{attempts}")
            print("❌ All retries failed")
        return wrapper
    return decorator


@retry(3)
def check_age():
    age = int(input("Enter age: "))
    print(age)

check_age()
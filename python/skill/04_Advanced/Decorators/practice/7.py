#access control

is_admin = False

def decorator(func):
    def wrapper(*args, **kwargs):
        if not is_admin:
          print("Access Denied! Admin only.")
          return None  
        return func(*args, *kwargs)
    return wrapper

@decorator
def login():
    print("Login successful! ")

login()
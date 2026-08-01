current_user = {
    "is_authenticated":True
}

def login_required(func):
    def wrapper(*args, **kwargs):
        if not current_user['is_authenticated']:
            print("❌ User not logged in!")
            return None
        return func(*args, **kwargs)
    return wrapper


@login_required
def dashboard():
    print("\033[92mUser logged in successfully\033[0m")


dashboard()
        
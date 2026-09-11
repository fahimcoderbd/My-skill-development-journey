data = {
    "user": {
        "name": "Fahim",
        "email": "fahim@gmail.com",
        "is_verified": True
    }
}

#printing user name and email and validating
def check_user(data):
    user = data.get("user", {})
    #name
    name = user.get("name")
    #email
    email = user.get("email")
    
    print(f"Name: {name}, email: {email}")

    if user.get("is_verified"):
        print("Verified")
    else:
        print("Not verified")
check_user(data)
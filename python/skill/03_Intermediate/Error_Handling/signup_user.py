#raise (python na parleo ,
# nije error dhore solve kora)

#example
#18 bosorer niche kew signup korte parbe na

def signup_user(age):
    try:
        if not isinstance(age, int):
            raise ValueError("Invalid input type")
        if age < 0:
            raise ValueError("Bhul input hoise")
        elif age < 18:
            raise ValueError("Tumi puchki")
        else:
            return "Signup successful"
    except ValueError as ve:
         return "signup failed: " + str(ve)
    
print(signup_user(16))  # Output: Tumi puchki
print(signup_user(20))  # Output: Signup successful
print(signup_user(-10))
print(signup_user("abc"))
print(signup_user(18.2))

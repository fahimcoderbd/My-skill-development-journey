'''
4. Login System 🔐
Scenario

ছোট্ট Login System।

Correct Credentials

username = admin
password = 1234

যদি ভুল username/password দেয়

raise PermissionError

except PermissionError

Access Denied

সঠিক হলে

Welcome Admin
'''

#sollution
admin_data = {
    'username':"admin",
    'password':1234
}

def admin_login(username: str, password:int):
    try:
        if username == admin_data['username'] and password == admin_data['password']:
           return "Welcome admin"
        else:
            raise PermissionError
        
    except PermissionError:
        return ("You are not an admin!, \n"
               "Access Denied"
        )

print(admin_login("Fahim", 1235))
print(admin_login("admin", 1234))
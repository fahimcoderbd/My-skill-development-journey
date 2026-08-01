import json

user_data = '''{
  "username": "fahim",
  "email": "fahim@gmail.com",
  "is_premium": false
}'''

#step 1 
#saving user data as json file
file_path = "json/data/data5.json"

def save_user(data):
    with open(file_path, 'w') as file:
         file.write(data)

save_user(user_data)

#step 3
#reading data and printing that data
def load_user():
    with open(file_path, 'r') as file:
        get_user_data = json.load(file)
        return get_user_data

print(load_user())


#step 4
#is_premium True => print
def update_item(key, value):
    if key not in load_user():
        return "The feature not found"
    else:
        load_user()
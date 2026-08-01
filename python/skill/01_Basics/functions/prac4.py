users = [
    {"name": "fahim", "active": True},
    {"name": "rahim", "active": False},
    {"name": "karim", "active": True},
]

# 1. শুধু active user গুলোর নাম বের করো
# 2. check করো সবাই active কিনা
# 3. active user কয়জন

active_users = []

for user in users:
    if user["active"] == True:
        active_users.append((user["name"]))
        print(f"active user: {user['name']}")

#2 checking all is active or not
all_active = all(u["active"] for u in users)
print(all_active)

#3 checkin len
check_len = len(active_users)
print(check_len)
notifications = [
    {"id": 1, "read": False},
    {"id": 2, "read": True},
    {"id": 3, "read": False}
]

def unread_notification(notifi):
     counter = 0
     for data in notifi:
         if not data['read']: 
            counter += 1
     return counter

final_data = unread_notification(notifications)
print(f"Unread notifications: {final_data}")
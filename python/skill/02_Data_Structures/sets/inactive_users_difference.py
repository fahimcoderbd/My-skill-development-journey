#problem 3

registered_users = {"fahim", "rahim", "karim", "sadia", "nabila"}
active_users = {"rahim", "karim"}

'''steps 

1.task1 =>
Find users who are inactive

i will use this active_users - registered_users

2.task2 =>
Count how many inactive users there are

i will count the length of the set found in task1

'''
#task 1
inactive_user = registered_users - active_users
print("Inactive users:", inactive_user)

#task2
count = len(inactive_user)
print("Number of inactive users:", count)

#1.👉 কয়জন ইউনিক user login করেছে?

logins = ["fahim", "rahim", "fahim", "karim", "rahim"]

unique = len(set(logins))
print(f"Unique logins: {unique}") 


#2
nums = [1, 2, 3, 3, 4, 5, 5, 6]
print(set(nums))  

#3
banned_users = ["bot", "scammer", "hacker", "admin"]

if "admin" in banned_users:
    print("Yes, admin is banned.")

#4
class_a = ["Fahim", "Rahim", "Karim", "Sajib"]
class_b = ["Rahim", "Sajib", "Tuhin"]

common = set(class_a) & set(class_b)
print(f"Common students: {common}")

#5
names = ["Fahim", "rahim", "Karim", "fahim", "Tuhin", "Sajib"]

def solution(name):
    result = set()

    for n in name:
        if len(n) > 4:
            result.add(n.lower())
            
    print(result)

solution(names)


#6
nums = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9]

def nums(numbers):
    result = set()
    sum = 0
    for num in numbers:
        if num % 2 == 0:
           cube = num ** 3
           sum += cube
        result.add(cube)
    print("Sum of cubes of even numbers:", sum)

nums(nums)

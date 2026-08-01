''''
2. Student Age Verification 🎓
Scenario

স্কুলে ভর্তি হওয়ার জন্য বয়স চেক করা হবে।

Rules
Age input নাও
যদি age < 5
raise ValueError
যদি age > 100
raise ValueError
নাহলে
Admission Allowed

Bonus

except ValueError:
    print("Invalid Age")
'''

#solution =>
def age_checker(age:int):
    try:
       if age < 5:
           raise ValueError
       elif age > 100:
           raise ValueError
       else:
           return "Admission Allowed"
       
    except ValueError:
         return "Invalid Age"

print(age_checker(4))
print(age_checker(1000))
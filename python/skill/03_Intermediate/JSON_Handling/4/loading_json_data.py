import json

path = "json/4/1.json"

#loading json data
with open(path, 'r') as file:
      students_data = json.load(file)
      
#counting total students
#counting present students
present_students = 0
absent_students = 0
total_students = len(students_data.get("students", []))

for student in students_data.get("students" ,[]):
    if student["present"]:
       present_students += 1
    else:
        absent_students += 1

print(f"Total students: {total_students}")
print(f"Present: {present_students}")
print(f"Absent: {absent_students}")
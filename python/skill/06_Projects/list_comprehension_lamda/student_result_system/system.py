students = [
    {"name": "Fahim", "marks": 95},
    {"name": "Rahim", "marks": 60},
    {"name": "Karim", "marks": 82},
    {"name": "Sakib", "marks": 40},
]

#task-1 Get all student names.
student_names = [student['name'] for student in students]

#task-2 Find students with marks ≥ 80.
students_with_marks = [student for student in students if student['marks'] >= 80]

#task-3 Sort by highest marks.
students.sort(key=lambda student: student['marks'], reverse=True)

#task-4 Find the student with the highest marks using max(..., key=lambda ...).
student_with_highest_mark = max(students, key=lambda student: student['marks'])

#testing
print(student_names)
print(students_with_marks)
print(student_with_highest_mark)

students = [
    {"name": "Fahim", "marks": 90},
    {"name": "Rahim", "marks": 70},
    {"name": "Karim", "marks": 95}
]

#amake lambda use kore students marks ascending order e sort korte hobe
students.sort(key=lambda student: student['marks'])
print(students)
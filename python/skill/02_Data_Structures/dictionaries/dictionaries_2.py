
students = {
    "Rahim": [80, 75, 90],
    "Karim": [60, 70, 65],
    "Fahim": [88, 92, 85]
}

result = {name: sum(mark) for name,mark in students.items()}
print(result)


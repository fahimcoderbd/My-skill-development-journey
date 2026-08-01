employees = [
    ["Rahim", 45000],
    ["Karim", 30000],
    ["Fahim", 60000],
    ["Sakib", 50000]
]

employees.sort(key=lambda employee: employee[1])

print(employees)
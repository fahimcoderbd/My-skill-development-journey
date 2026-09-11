employees = [
    {"name": "A", "salary": 25000},
    {"name": "B", "salary": 70000},
    {"name": "C", "salary": 45000},
    {"name": "D", "salary": 90000},
]

#task-1 Get all salaries.
all_salaries = [employee['salary'] for employee in employees]

#task-2 Find employees earning more than 50,000.
employees_earning_more = [employee for employee in employees if employee['salary'] > 50000]

#task-3 Sort by salary (highest first).
employees.sort(key=lambda employee: employee['salary'], reverse=True)

#task-4 Find the highest-paid employee.
highest_paid_employee = max(employees, key=lambda employee: employee['salary'])

#testing
print(all_salaries)
print(employees_earning_more)
print(highest_paid_employee)
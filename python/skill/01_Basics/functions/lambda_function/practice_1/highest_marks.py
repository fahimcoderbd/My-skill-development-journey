students = [
    {"name": "Fahim", "marks": 80},
    {"name": "Ali", "marks": 95},
    {"name": "Rahim", "marks": 70}
]

def highest_marks(arr):
    if not arr:
        return None
    
    highest = max(arr, key=lambda x: x["marks"])

    return highest

print(highest_marks(students))
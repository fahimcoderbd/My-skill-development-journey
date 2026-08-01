def tuple_list_sorting(arr):
    if not arr:
        return None
    
    sorted_list = list(sorted(arr, key=lambda x: x[1]))

    return sorted_list

students = [
    ("Fahim", 80),
    ("Ali", 95),
    ("Rahim", 70)
]

print(tuple_list_sorting(students))
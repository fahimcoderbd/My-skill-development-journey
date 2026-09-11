#student marks analyzer
#14/8/26

def marks_analyzer(marks:list):
    if not marks : return

    highest_mark = max(marks)
    lowest_mark = min(marks)
    average_mark = sum(marks) / len(marks)
    marks_80_up = 0

    for mark in marks:
        if mark >= 80: marks_80_up += 1

    return (
        f"Highest mark: {highest_mark} \n"
        f"Lowest mark: {lowest_mark} \n"
        f"Average mark: {average_mark:.2f} \n"
        f"80+ : {marks_80_up}"
    )

print(marks_analyzer([]))
print(marks_analyzer([72, 85, 91, 64, 78, 88, 95]))
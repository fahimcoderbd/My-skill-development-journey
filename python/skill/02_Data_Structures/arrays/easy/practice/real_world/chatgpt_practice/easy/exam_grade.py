'''
Problem 2 — পরীক্ষার গ্রেড বের করো

📝 তোমার ক্লাসের সব students-এর marks আছে। প্রতিটার জন্য grade assign করো এবং কতজন pass করেছে সেটাও বলো।
marks list দেওয়া থাকবে। প্রতিটার জন্য grade বের করো: 80+ = A, 60-79 = B, 40-59 = C, 40 এর নিচে = F (Fail)। তারপর মোট pass count return করো।

marks = [85, 37, 72, 55, 91, 40, 63]

Output:
Grades: ['A', 'F', 'B', 'C', 'A', 'C', 'B']
Pass: 5, Fail: 2
'''

def num_to_grade(num):
    # Ekhane direct return kore dile 'grade' variable lagbe na ebong code ektu faka hobe
    if num >= 80:
        return 'A'
    elif num >= 60:   # 80 er choto eta automatic check hoye jacche
        return 'B'
    elif num >= 40:   # 60 er choto eta check hoye jacche
        return 'C'
    else:
        return 'F'
        

def exam_grade_calculator(arr):
    if not arr:
        return None
    
    grades = []
    passed_students = 0
    failed_students = 0

    for num in arr:
        grade = num_to_grade(num)
        grades.append(grade)
        
        if grade != 'F':
            passed_students += 1
        else:
            failed_students += 1

    # Khub readable output er jonno string join kora holo
    grades_str = ", ".join(grades) 
    return f"Grades: [{grades_str}] | Pass: {passed_students}, Fail: {failed_students}"

# Test cases
marks = [85, 37, 72, 55, 91, 40, 63]
print(exam_grade_calculator(marks))


    






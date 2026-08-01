def result(*mark , **student_info):
    if not mark:
     print("No marks provided!")
     return
    #average of marks
    average = sum(mark) / len(mark)

    #printing user info and result
    for key,data in student_info.items():
        print(f"{key} : {data}")
    
    print(f"Average: {average}")

    if average >= 40:
        print("You passed successfully!")
    else:
        print("Sorry, you failed!")

result(name="Rahim", class_="9")
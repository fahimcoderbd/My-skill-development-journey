import os
from os import path

class Student:
    def __init__(self, name:str, roll:int, marks:float):
        self.name = name #student's name
        self.roll = roll #student's roll
        self.marks = marks #student's marks

    #check pass
    def is_pass(self) -> bool:
        return self.marks >= 33

    #display student's info
    def display_info(self):
        status = "Pass" if self.is_pass() else "Fail"

        return (
            f"Name: {self.name} \n"
            f"Roll: {self.roll} \n"
            f"Marks: {self.marks} \n"
            f"Status: {status} \n"
        )

student_1 = Student(name="Fahim", roll=12, marks=32)
print(student_1.display_info())

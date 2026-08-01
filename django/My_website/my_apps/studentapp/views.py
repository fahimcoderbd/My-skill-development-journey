from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . import models


# Home / Student page
def student_view(request):
    return render(request, 'templates/studentapp/student_page.html')


# CREATE (Add Student)
def add_view(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        student_class = request.POST.get('student_class')

        models.Student.objects.create(
            name=name,
            email=email,
            age=age,
            student_class_value=student_class
        )

        messages.success(request, "Student created successfully!")

        return redirect('/student')

    return render(request, 'templates/studentapp/add_student.html')


# READ (Show All Students)
def show_view(request):

    students = models.Student.objects.all()

    return render(
        request,
        'templates/studentapp/show_students.html',
        {'students': students}
    )


# UPDATE Student
def update_view(request, id):

    student = get_object_or_404(models.Student, id=id)

    if request.method == "POST":

        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        student.student_class_value = request.POST.get('student_class')

        student.save()

        messages.success(request, "Student updated successfully!")

        return redirect('/student')

    return render(
        request,
        'templates/studentapp/update_student.html',
        {'student': student}
    )


# DELETE Student
def delete_view(request, id):

    student = get_object_or_404(models.Student, id=id)

    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully!")
        return redirect('/student')

    return render(
        request,
        'templates/studentapp/delete_student.html',
        {'student': student}
    )
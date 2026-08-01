from django.db import models

# Create your models here.
#OnetoOne model practice-2
class Student(models.Model):
      name = models.CharField(max_length=100)
      email = models.EmailField()
      student_class = models.IntegerField(max_length=10)
      department = models.CharField(max_length=50)

      def __str__(self):
           return self.name

class StudentProfile(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE
    )
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
         return self.student.name
from django.db import models

# Create your models here.

class Course(models.Model):
      name = models.CharField(max_length=100, blank=False)
      duration = models.FloatField()
      fees = models.IntegerField()
      teacher = models.CharField(max_length=100, blank=False)

      def __str__(self):
            return self.name
      
class Student(models.Model):
      name = models.CharField(max_length=100, blank=False)
      phone = models.IntegerField()
      email = models.EmailField()
      course = models.ManyToManyField(Course, related_name="courses")

      def __str__(self):
            return self.name

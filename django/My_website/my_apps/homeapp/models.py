from django.db import models

# Create your models here.

class Contact(models.Model):
     
     #fields
     name = models.CharField(max_length=50)
     email = models.EmailField()
     message = models.CharField(max_length=150)
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.name
     
class Product(models.Model):
     name = models.CharField(max_length=50)
     price = models.IntegerField()
     description = models.CharField(max_length=300)
     created_at = models.DateTimeField(auto_now_add=True)
     category = models.CharField(
          max_length=20,
          default="General"
          )

     def __str__(self):
          return self.name
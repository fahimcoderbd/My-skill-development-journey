from django.db import models

# Create your models here.
#Author model
class Author(models.Model):
    name = models.CharField(max_length=100, blank=False)
    contact = models.EmailField(blank=False)

    def __str__(self):
        return self.name
    
#Book model (book can have one or more authors)
class Book(models.Model):
     name = models.CharField(max_length=100, blank=False)
     category = models.CharField(max_length=100, blank=False)
     language = models.CharField(max_length=50, blank=False)
     edition = models.IntegerField()
     author = models.ManyToManyField(
         Author, related_name="authors"
     )

     def __str__(self):
         return self.name

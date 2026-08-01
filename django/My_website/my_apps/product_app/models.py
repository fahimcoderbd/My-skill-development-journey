from django.db import models

# Create your models here.

class ProductX(models.Model):
     name = models.CharField(max_length=50)
     price = models.IntegerField()
     description = models.CharField(max_length=300)
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.description
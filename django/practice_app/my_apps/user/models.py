from django.db import models

# Create your models here.
#one to one field practice
#user => profile
class User(models.Model):
      user_name = models.CharField(max_length=100, blank=False)
      user_email = models.EmailField(blank=False)
      user_password = models.CharField(max_length=100, blank=False)

      def __str__(self):
            return self.user_name
      
class profile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Create_user")
      bio = models.TextField()

      def __str__(self):
            return self.user.user_name
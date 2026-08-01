from django.db import models

# Create your models here.
#author and notes models
class Author(models.Model):
      name = models.CharField(max_length=100)

      def __str__(self):
            return self.name
      
class Note(models.Model):
      title = models.CharField(max_length=100)

      author = models.ForeignKey(
            Author,
            on_delete=models.PROTECT,
            null=True,
            related_name="notes"
      )

      def __str__(self):
            return self.title
      

#user and images model
#user can upload images on site
class User(models.Model):
      name = models.CharField(max_length=100)
      email = models.EmailField()

      def __str__(self):
            return self.name

class UserImage(models.Model):
      image = models.ImageField(upload_to="author_images/", blank=True, null=True)
      user = models.ForeignKey(
       User,
       on_delete=models.PROTECT,
       related_name="user_data"
      )

      def __str__(self):
            return self.user.name

#pdfs and categories model
class DocFile(models.Model):
      name = models.CharField(max_length=100)
      pdf = models.FileField(upload_to='documents')

      def __str__(self):
            return self.name

class DocCategory(models.Model):
      category = models.CharField(max_length=100)

      doc_data = models.ForeignKey(
            DocFile,
            on_delete=models.PROTECT,
            related_name='pdf_files'
      )

      def __str__(self):
            return self.doc_data.name
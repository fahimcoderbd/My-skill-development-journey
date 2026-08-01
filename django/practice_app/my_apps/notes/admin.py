from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Author)
admin.site.register(models.Note)

#user and images
admin.site.register(models.User)
admin.site.register(models.UserImage)

#pdfs and category
admin.site.register(models.DocCategory)
admin.site.register(models.DocFile)
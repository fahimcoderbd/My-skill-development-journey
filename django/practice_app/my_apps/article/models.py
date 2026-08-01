from django.db import models
from django.utils import timezone

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('D', 'Draft'),
        ('S', 'Sci-Fi'),
    ]

    title = models.CharField(max_length=150)
    content = models.TextField()
    category = models.CharField(
        max_length=1,
        choices=CATEGORY_CHOICES,
        blank=True
    )

    created_at = models.DateTimeField(default=timezone.now)

    author = models.CharField(max_length=100, default="Fahim Abrar")
    author_email = models.EmailField(default="artipeai@gmail.com")

    author_image = models.ImageField(upload_to="media/author_images/", blank=True, null=True)
    document_file = models.FileField(upload_to="media/documents/", blank=True, null=True)

    def __str__(self):
        return self.title
    

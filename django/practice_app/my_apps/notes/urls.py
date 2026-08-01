from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.notes_home, name="notes_homepage"),
    path("author" ,views.show_author_name, name="showing author name from db"),
    path("author_notes", views.get_article_from_author, name="author's notes")
]
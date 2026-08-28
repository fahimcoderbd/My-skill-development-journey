from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.homeapp, name='books-homepage'),

    #many to many operations
    path('add_books/', views.add_books, name='books-to-authors'),
    path('remove_books/', views.remove_books, name='remove-books-from-authors'),
    path('set_books/', views.set_books, name='set-books-for-authors'),
    path('clear_books/', views.clear_books, name='clear-books-from-authors'),
    path('all_books/', views.all_books, name='all-books-for-authors'),
    path('all_authors/',views.show_all_authors, name='showing-all-authors' ),
    path('filter_author_by_name/',views.filtering_by_author_name, name='searching-author-by-name'),
    path('filter_author_by_book', views.filtering_by_book_name, name='searching-author-by-book')
]
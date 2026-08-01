from django.urls import path
from . import views

#creating app routes
urlpatterns = [
    path('' ,views.student_view, name='student'),
    path('add_student/' , views.add_view, name="add"),
    path('show_students/' , views.show_view , name="show"),
    path('update_student/<int:id>' , views.update_view, name="update"),
    path('delete_student/<int:id>' , views.delete_view, name="delete")
]
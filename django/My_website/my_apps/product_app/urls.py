from django.urls import path
from . import views

urlpatterns = [

path('', views.dashboard_view, name="Products app"),
path('show_products/', views.show_products_view, name="Products app"),


]

from django.shortcuts import render
from . import models

# Create your views here.

def dashboard_view(request):

    return render(request , 'templates/productapp/dasboard.html')

def show_products_view(request):

    return render(request , 'templates/productapp/show_products.html')
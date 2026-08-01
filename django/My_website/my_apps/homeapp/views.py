from django.shortcuts import render,redirect
from . import models

# Create your views here.

def home_view(request):
    return render(request, 'templates/homeapp/home.html')


def about_view(request):
    return render(request, 'templates/homeapp/about.html')

def contact_data_view(request):
    #getting contact data
    contact_data = models.Contact.objects.all()

    #returning data as dictionary
    return render(request, 'templates/homeapp/contact_view.html' , {'contact_data':contact_data}) 



def contact_view(request):
    submitted = False
    if request.method == 'POST':
        submitted = True
       
       #taking inputs from user
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        #creating data to db
        models.Contact.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        #after creating db redirecting user to show the contact details
        return redirect('/contact_info')

    return render(request, 'templates/homeapp/contact.html', {'submitted': submitted})





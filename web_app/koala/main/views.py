from django.http.response import HttpResponse 
from django.shortcuts import render 

# Create your views here.


def home_page(request):
    return render(request,"home.html") 


def contact_us(request):
    if request.method == "POST":
       request_data = dict(request.POST) 
       request_data.pop 
       ('csrfmiddlewaretoken') 
       data = {key:request_data.get(key)[0]
       for key in request_data}
       print(data)  

    
    return render(request, "contact.html")


def about_us(request):
    return render(request, "about.html")

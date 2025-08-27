from django.http import HttpResponse
from django.shortcuts import render 

def home(request):
    return render(request, "websites/index.html")

def about(request):
    #return HttpResponse("About us")
    return render(request, "websites/about.html")

def contact(request):
    return render(request, "websites/contact.html")
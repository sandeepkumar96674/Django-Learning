from django.shortcuts import render
from .models import Student

# Create your views here.
def all_app(request):
    student = Student.objects.all()
    return render(request, "myapp/all_app.html", {"students": student})

def form_app(request):
    return render(request, "myapp/forms.html")
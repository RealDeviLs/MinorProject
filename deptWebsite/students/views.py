from django.shortcuts import render
from .models import Student
# Create your views here.

def alumni_page(request):
    alumni = Student.on_site.filter(isAlumni=True)
    data = {
        "alumni":alumni
    }
    return render(request, template_name='alumni.html',context=data)
from django.shortcuts import render

from .models import Student
from django.db.models import Q

# Create your views here.


def alumni_page(request):
    alumni = Student.on_site.filter(isAlumni=True)
    if request.method == 'POST':
        string = request.POST["queryString"]
        if string is not None:
            if(string.isdigit()):
                batchq = Q(batch__icontains= int(string))
                alumni =   alumni.filter(Q(name__icontains=string) | Q(course__icontains=string) | Q(placements__company__icontains=string) | Q(internships__company__icontains=string) | batchq).distinct()
            else:
                alumni =   alumni.filter(Q(name__icontains=string) | Q(course__icontains=string) | Q(placements__company__icontains=string) | Q(internships__company__icontains=string)).distinct()
        data = {
                "alumni": alumni
            }
        return render(request, 'alumni.html', context=data)   
    data = {"alumni": alumni}
    return render(request, template_name="alumni.html", context=data)

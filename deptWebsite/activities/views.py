from django.shortcuts import render

# Create your views here.


def activities(request):

    return render(request, template_name='activities.html')
from django.shortcuts import render

# Create your views here.


def infrastructure(request):

    return render(request, template_name='infrastructure.html')
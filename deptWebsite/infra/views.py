from django.shortcuts import render
from .models import Infra,InfraImage
# Create your views here.


def infra(request):
    infra = Infra.objects.all() 
    data ={
        "infra": infra
    }
    return render(request,template_name="infra.html",context=data)
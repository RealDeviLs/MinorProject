from django.shortcuts import render

from .models import Infra

# Create your views here.


def infra(request):
    infra = Infra.on_site.all()
    data = {"infra": infra}
    return render(request, template_name="infra.html", context=data)

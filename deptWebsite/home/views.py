from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from academics.models import AcademicProgram
# Create your views here.
from whitelabel.models import WhiteLabel


def home_page(request):
    print(get_current_site(request))
    print(settings.SITE_ID)
    academic_program =AcademicProgram.on_site.all()[0]
    peo = academic_program.peo.all()
    btech=peo[0]
    mtech=peo[1]
    phd=peo[2]
    print(btech.description)
    return render(request,template_name="index.html",context={'btech':btech,'mtech':mtech,'phd':phd})

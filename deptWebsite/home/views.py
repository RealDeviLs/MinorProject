from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
# Create your views here.
from whitelabel.models import WhiteLabel


def home_page(request):
    print(get_current_site(request))
    print(settings.SITE_ID)
    print( WhiteLabel.on_site.all()[0].department_name)
   
    return render(request,template_name="index.html")
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render

# Create your views here.
from whitelabel.models import WhiteLabel


def home_page(request):
    print(get_current_site(request))
    print(settings.SITE_ID)
    basic_data = WhiteLabel.on_site.first()
    data = {
        "basic": basic_data,
    }
    return render(request, template_name="index.html", context=data)

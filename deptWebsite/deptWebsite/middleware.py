from django.conf import settings
from django.contrib.sites.models import Site
from django.core.cache import cache

from django.http import HttpResponse

class SiteMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        try:
            current_site = Site.objects.get(domain=request.get_host())
        except Site.DoesNotExist:
            current_site = Site.objects.get(id=settings.SITE_ID)

        request.current_site = current_site
        settings.SITE_ID = current_site.id
        response = self.get_response(request)
        return response

        
    def process_request(self, request):
        print("eteje")
        try:
            current_site = Site.objects.get(domain=request.get_host())
        except Site.DoesNotExist:
            current_site = Site.objects.get(id=settings.SITE_ID)

        request.current_site = current_site
        settings.SITE_ID = current_site.id
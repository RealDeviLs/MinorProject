from django.conf import settings
from deptWebsite.settings import SITE_ID
from django.contrib.sites.models import Site


def DynamicSiteMiddleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        try:
            current_site = Site.objects.get(domain=request.get_host())
        except Site.DoesNotExist:
            current_site = Site.objects.get(id=settings.SITE_ID)
        request.site = current_site
        settings.SITE_ID = current_site.id
        SITE_ID = current_site.id
        print(settings.SITE_ID)
        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
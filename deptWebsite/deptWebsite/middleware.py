from django.conf import settings
from django.contrib.sites.models import Site
from faculty.models import DeptPerson
from whitelabel.models import WhiteLabel


def DynamicSiteMiddleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        try:
            current_site = Site.objects.get(domain=request.get_host())
        except Site.DoesNotExist:
            current_site = Site.objects.get(id=settings.SITE_ID)
        request.site = current_site
        settings.SITE_ID = current_site.id
        current_site.id
        print(settings.SITE_ID)
        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware


def send_person_id_to_base(request):

    department = WhiteLabel.on_site.first()
    if request.user.is_authenticated:
        person = DeptPerson.on_site.filter(user=request.user).first()
        if person:
            return {"person": person.id, "department": department}

    return {"person": None, "department": department}

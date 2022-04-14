from django.shortcuts import get_object_or_404, render

from .models import Activity

# Create your views here.


def activities(request):
    activities = Activity.on_site.all()
    data = {"activities": activities}
    return render(request, template_name="activities.html", context=data)


def activity_detail(request, id):
    activity = get_object_or_404(Activity, id=id)
    data = {"activity": activity, "images": activity.images.all()}
    return render(request, template_name="activity_detail.html", context=data)

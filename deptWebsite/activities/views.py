from django.shortcuts import render
from .models import Activity,ActivityImage
from django.shortcuts import get_object_or_404

# Create your views here.


def activities(request):
    activities = Activity.objects.all()

    print(activities)
    data = {
        "activities":activities
    }
    return render(request, template_name='activities.html',context = data)


def activity_detail(request,id):
    print(request.site)
    activity =get_object_or_404(Activity,id=id)
    data = {
        "activity": activity,
        "images": activity.images.all()
    }
    print( activity.images.all()[0].image.url)
    return render(request, template_name='activity_detail.html',context =data)
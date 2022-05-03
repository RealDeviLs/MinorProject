from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404, redirect, render
from faculty.models import DeptPerson

from .forms import ActivityForm
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


def show_activities(request):

    user = request.user
    person = DeptPerson.on_site.filter(user=user).first()

    if person.dept_edit_access:
        return render(
            request,
            template_name="error.html",
            context={
                "code": 401,
                "message": "you do not have permissions to edit this page",
            },
        )

    if request.method == "POST":

        instance = Activity(department=get_current_site(request))
        data = ActivityForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")

    table_data = Activity.on_site.all()
    form = ActivityForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "edit_activity"}
    return render(request, template_name="showTable.html", context=data)


def edit_activity(request, id):

    instance = Activity.on_site.filter(id=id).first()
    # id = instance.person.id
    form = ActivityForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
            return redirect("edit_activity", id)
        data = ActivityForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("edit_activity", id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from faculty.models import DeptPerson

from .forms import InfraForm
from .models import Infra

# Create your views here.


def infra(request):
    infra = Infra.on_site.all()
    data = {"infra": infra}
    return render(request, template_name="infra.html", context=data)


# Create your views here.


def show_infra(request):

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

        instance = Infra(department=get_current_site(request))
        data = InfraForm(request.POST, request.FILES, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")

    table_data = Infra.on_site.all()
    form = InfraForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "edit_infra"}
    return render(request, template_name="showTable.html", context=data)


def edit_infra(request, id):

    instance = Infra.on_site.filter(id=id).first()
    # id = instance.person.id
    form = InfraForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
            return redirect("edit_infra", id)
        data = InfraForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("edit_infra", id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)

# Create your views here.
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from faculty.models import DeptPerson

from .forms import AcademicProgramForm
from .models import AcademicProgram

# Create your views here.


def show_academic_programs(request):

    user = request.user
    person = DeptPerson.on_site.filter(user=user).first()

    if not person.dept_edit_access:
        return render(
            request,
            template_name="error.html",
            context={
                "code": 401,
                "message": "you do not have permissions to edit this page",
            },
        )

    if request.method == "POST":

        instance = AcademicProgram(department=get_current_site(request))
        data = AcademicProgramForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")

    table_data = AcademicProgram.on_site.all()
    form = AcademicProgramForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "edit_academic"}
    return render(request, template_name="showTable.html", context=data)


def edit_academic_program(request, id):

    instance = AcademicProgram.on_site.filter(id=id).first()
    # id = instance.person.id
    form = AcademicProgramForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
            return redirect("edit_academic", id)
        data = AcademicProgramForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("edit_academic", id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)

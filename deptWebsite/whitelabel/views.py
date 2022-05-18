from django.contrib import messages
from django.shortcuts import redirect, render
from students.models import Student

from .forms import SocietyClubForm, WhiteLabelForm
from .models import SocietyClub, WhiteLabel

# Create your views here.


def create_dept(request):

    if request.method == "POST" and request.POST.get("type") == "basic":
        white_label = WhiteLabel.on_site.first()
        data = WhiteLabelForm(request.POST, request.FILES, instance=white_label)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")
    batches = Student.on_site.all().values("batch").distinct()

    white_label = WhiteLabel.on_site.first()
    if white_label:
        white_label_form = WhiteLabelForm(instance=white_label)
    else:
        white_label_form = WhiteLabelForm()
    clubs = SocietyClub.objects.filter(dept=white_label)
    club_form = SocietyClubForm()
    data = {
        "department":white_label,
        "form": white_label_form,
        "clubs": clubs,
        "club_form": club_form,
        "batches": batches,
    }
    return render(request, template_name="create_dept.html", context=data)


def add_club(request):

    white_label = WhiteLabel.on_site.first()
    if request.method == "POST":
        instance = SocietyClub(dept=white_label)
        data = SocietyClubForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
        else:
            print(data.errors)
            messages.error(request, f"failed to save, {data.errors}")
        return redirect("create_dept")
    else:
        return render(
            request,
            template_name="error.html",
            context={
                "code": 401,
                "message": "you do not have permissions to edit this page",
            },
        )


def edit_club(request, id):

    instance = SocietyClub.objects.filter(id=id).first()
    form = SocietyClubForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            SocietyClub.objects.filter(id=id).delete()
            return redirect("create_dept")
        data = SocietyClubForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("create_dept")
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)

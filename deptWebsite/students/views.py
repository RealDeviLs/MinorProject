from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import InternshipForm, PlacementForm, ProjectForm, StudentForm
from .models import Internship, Placement, Project, Student

# Create your views here.


def alumni_page(request):
    alumni = Student.on_site.filter(is_alumni=True)
    if request.method == "POST":
        string = request.POST["queryString"]
        if string is not None:
            if string.isdigit():
                batchq = Q(batch__icontains=int(string))
                alumni = alumni.filter(
                    Q(name__icontains=string)
                    | Q(course__icontains=string)
                    | Q(placements__company__icontains=string)
                    | Q(internships__company__icontains=string)
                    | batchq
                ).distinct()
            else:
                alumni = alumni.filter(
                    Q(name__icontains=string)
                    | Q(course__icontains=string)
                    | Q(placements__company__icontains=string)
                    | Q(internships__company__icontains=string)
                ).distinct()
        data = {"alumni": alumni}
        return render(request, "alumni.html", context=data)
    data = {"alumni": alumni}
    return render(request, template_name="alumni.html", context=data)


def show_for_edit(request, batch):

    table_data = Student.on_site.filter(batch=batch).order_by("roll_number").all()

    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"table_data": table_entries, "type": "edit_infra"}

    return render(request, "show_for_edit.html", context=data)


def edit_basic_student(request, id):
    student = Student.on_site.filter(id=id).first()

    if student:
        form = StudentForm(instance=student)
    else:
        form = StudentForm()
        data = StudentForm(request.POST, request.FILES, instance=student)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")

    if request.method == "POST" and request.POST.get("type") == "basic":
        data = StudentForm(request.POST, request.FILES, instance=student)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")

    student = Student.on_site.filter(id=id).first()
    internships = Internship.objects.filter(person=student).all()
    placements = Placement.objects.filter(person=student).all()
    projects = Project.objects.filter(person=student).all()

    data = {
        "student": student,
        "form": form,
        "internships": internships,
        "placements": placements,
        "projects": projects,
        "internship_form": InternshipForm(),
        "placement_form": PlacementForm(),
        "project_form": ProjectForm(),
    }

    return render(request, template_name="basic_student.html", context=data)


def add_internship(request, id):

    student = Student.on_site.filter(id=id).first()

    if request.method == "POST":
        instance = Internship(person=student)
        data = InternshipForm(request.POST, instance=instance)

    if data.is_valid():
        data.save()
        messages.success(request, "Saved")

    else:
        messages.error(request, f"failed to save, {data.errors}")

    return redirect("edit_basic_student", id)


def edit_internship(request, id):

    instance = Internship.objects.filter(id=id).first()
    person_id = instance.person.id
    form = InternshipForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
            return redirect("edit_basic_student", person_id)
        data = InternshipForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("edit_basic_student", person_id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)


def add_placement(request, id):

    student = Student.on_site.filter(id=id).first()

    if request.method == "POST":
        instance = Placement(person=student)
        data = PlacementForm(request.POST, instance=instance)

    if data.is_valid():
        data.save()
        messages.success(request, "Saved")

    else:
        messages.error(request, f"failed to save, {data.errors}")

    return redirect("edit_basic_student", id)


def edit_placement(request, id):

    instance = Placement.objects.filter(id=id).first()
    person_id = instance.person.id
    form = PlacementForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
            return redirect("edit_basic_student", person_id)
        data = PlacementForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("edit_basic_student", person_id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)


def add_project(request, id):
    student = Student.on_site.filter(id=id).first()

    if request.method == "POST":
        instance = Project(person=student)
        data = ProjectForm(request.POST, instance=instance)

        if data.is_valid():
            data.save()
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")

    return redirect("edit_basic_student", id)


def edit_project(request, id):

    instance = Project.objects.filter(id=id).first()
    person_id = instance.person.id
    form = ProjectForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
            return redirect("edit_basic_student", person_id)
        data = ProjectForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("edit_basic_student", person_id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)

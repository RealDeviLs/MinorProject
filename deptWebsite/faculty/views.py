from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    AffilationForm,
    AwardForm,
    BasicProfileForm,
    BookPublicationForm,
    ConferencePublicationForm,
    EventForm,
    JournalPublicationForm,
    PatentForm,
    PGDissertationGuidedForm,
    PhDSupervisedForm,
    ProfileLinksForm,
    ProjectForm,
    ResearchInfoForm,
    ResponsibilityForm,
)
from .models import (
    Affilation,
    Award,
    BookPublication,
    ConferencePublication,
    DeptPerson,
    Event,
    JournalPublication,
    Patent,
    PGDissertationGuided,
    PhDSupervised,
    ProfileLinks,
    Project,
    ResearchInfo,
    Responsibility,
)

# Create your views here.


def faculty_page(request):
    faculty = DeptPerson.on_site.all()
    data = {"faculty": faculty}
    return render(request, template_name="faculty_page.html", context=data)


def faculty_detail(request, id):
    profile = get_object_or_404(DeptPerson, id=id)
    profile_links = (
        profile.profile_links.content if hasattr(profile, "profile_links") else None
    )
    research_info = (
        profile.research_info.content if hasattr(profile, "research_info") else None
    )
    journal_publications = profile.journal_publications.all()
    conference_publications = profile.conference_publications.all()
    book_publications = profile.book_publications.all()
    research_projects = profile.projects.all()
    events = profile.events.all()
    affilations = profile.affilations.all()
    phd_scholars = profile.phd_scholars.all()
    pg_students = profile.pg_students.all()
    patents = profile.patents.all()
    responsibilities = profile.responsibilities.all()
    data = {
        "profile": profile,
        "profile_links": profile_links,
        "research_info": research_info,
        "journal_publications": journal_publications,
        "conference_publications": conference_publications,
        "book_publications": book_publications,
        "research_projects": research_projects,
        "events": events,
        "affilations": affilations,
        "phd_scholars": phd_scholars,
        "pg_students": pg_students,
        "patents": patents,
        "responsibilities": responsibilities,
        "awards": profile.awards.all(),
    }
    return render(request, template_name="profile.html", context=data)


def edit_basic(request, id):

    person = DeptPerson.on_site.filter(id=id).first()
    if person:
        basic_form = BasicProfileForm(instance=person)
    else:
        basic_form = BasicProfileForm()

    if request.method == "POST" and request.POST.get("type") == "basic":
        data = BasicProfileForm(request.POST, request.FILES, instance=person)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")

    person = DeptPerson.on_site.filter(id=id).first()
    if person:
        basic_form = BasicProfileForm(instance=person)
    else:
        basic_form = BasicProfileForm()

    profile_links = ProfileLinks.objects.filter(person=person).all()
    research_info = ResearchInfo.objects.filter(person=person).all()
    profile_link_form = ProfileLinksForm()
    research_info_form = ResearchInfoForm()
    data = {
        "person": person,
        "form": basic_form,
        "profile_links": profile_links,
        "profile_link_form": profile_link_form,
        "research_info": research_info,
        "research_info_form": research_info_form,
    }
    return render(request, template_name="edit_basic.html", context=data)


def show_journal_publications(request, person_id):

    user = request.user
    person = DeptPerson.on_site.filter(user=user).first()
    if not person.id == person_id or not person:
        return render(
            request,
            template_name="error.html",
            context={
                "code": 401,
                "message": "you do not have permissions to edit this page",
            },
        )

    if request.method == "POST":
        instance = JournalPublication(person=person)
        data = JournalPublicationForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")

    table_data = JournalPublication.objects.filter(person__id=person_id)

    form = JournalPublicationForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "Journal"}
    return render(request, template_name="showTable.html", context=data)


def show_conf_publications(request, person_id):
    user = request.user
    person = DeptPerson.on_site.filter(user=user).first()
    if not person.id == person_id:
        return render(
            request,
            template_name="error.html",
            context={
                "code": 401,
                "message": "you do not have permissions to edit this page",
            },
        )

    if request.method == "POST":
        instance = ConferencePublication(person=person)
        data = ConferencePublicationForm(request.POST, instance=instance)
        if data.is_valid():
            print(data)
            x = data.save()
            print(x)
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")

    table_data = ConferencePublication.objects.filter(person__id=person_id)
    form = ConferencePublicationForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "Conference"}
    return render(request, template_name="showTable.html", context=data)


# def
def show_book_publications(request, person_id):
    user = request.user
    person = DeptPerson.on_site.filter(user=user).first()
    if not person.id == person_id:
        return render(
            request,
            template_name="error.html",
            context={
                "code": 401,
                "message": "you do not have permissions to edit this page",
            },
        )

    if request.method == "POST":
        instance = BookPublication(person=person)
        data = BookPublicationForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")

    table_data = BookPublication.objects.filter(person__id=person_id)
    form = BookPublicationForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "Book"}
    return render(request, template_name="showTable.html", context=data)


def show_projects(request, person_id):

    user = request.user
    person = DeptPerson.on_site.filter(user=user).first()
    if not person.id == person_id:
        return render(
            request,
            template_name="error.html",
            context={
                "code": 401,
                "message": "you do not have permissions to edit this page",
            },
        )

    if request.method == "POST":
        instance = Project(person=person)
        data = ProjectForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")

    table_data = Project.objects.filter(person__id=person_id)
    form = ProjectForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "Project"}
    return render(request, template_name="showTable.html", context=data)


def show_events(request, person_id):
    user = request.user
    person = DeptPerson.on_site.filter(user=user).first()
    if not person.id == person_id:
        return render(
            request,
            template_name="error.html",
            context={
                "code": 401,
                "message": "you do not have permissions to edit this page",
            },
        )

    if request.method == "POST":
        instance = Event(person=person)
        data = EventForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")

    table_data = Event.objects.filter(person__id=person_id)
    form = EventForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "Events"}
    return render(request, template_name="showTable.html", context=data)


def show_affiliation(request, person_id):
    user = request.user
    person = DeptPerson.on_site.filter(user=user).first()
    if not person.id == person_id:
        return render(
            request,
            template_name="error.html",
            context={
                "code": 401,
                "message": "you do not have permissions to edit this page",
            },
        )

    if request.method == "POST":
        instance = Affilation(person=person)
        data = AffilationForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")
    table_data = Affilation.objects.filter(person__id=person_id)
    form = AffilationForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "Affiliation"}
    return render(request, template_name="showTable.html", context=data)


def show_phd(request, person_id):
    user = request.user
    person = DeptPerson.on_site.filter(user=user).first()
    if not person.id == person_id:
        return render(
            request,
            template_name="error.html",
            context={
                "code": 401,
                "message": "you do not have permissions to edit this page",
            },
        )

    if request.method == "POST":
        instance = PhDSupervised(person=person)
        data = PhDSupervisedForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")

    table_data = PhDSupervised.objects.filter(person__id=person_id)
    form = PhDSupervisedForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "PHD Scholars Guided"}
    return render(request, template_name="showTable.html", context=data)


def show_pgd(request, person_id):
    user = request.user
    person = DeptPerson.on_site.filter(user=user).first()
    if not person.id == person_id:
        return render(
            request,
            template_name="error.html",
            context={
                "code": 401,
                "message": "you do not have permissions to edit this page",
            },
        )

    if request.method == "POST":
        instance = PGDissertationGuided(person=person)
        data = PGDissertationGuidedForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")
    table_data = PGDissertationGuided.objects.filter(person__id=person_id)
    form = PGDissertationGuidedForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "PGD Guided"}
    return render(request, template_name="showTable.html", context=data)


def show_patent(request, person_id):
    user = request.user
    person = DeptPerson.on_site.filter(user=user).first()
    if not person.id == person_id:
        return render(
            request,
            template_name="error.html",
            context={
                "code": 401,
                "message": "you do not have permissions to edit this page",
            },
        )

    if request.method == "POST":
        instance = Patent(person=person)
        data = PatentForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")

    table_data = Patent.objects.filter(person__id=person_id)
    form = PatentForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "Patent"}
    return render(request, template_name="showTable.html", context=data)


def show_responsibility(request, person_id):
    user = request.user
    person = DeptPerson.on_site.filter(user=user).first()
    if not person.id == person_id:
        return render(
            request,
            template_name="error.html",
            context={
                "code": 401,
                "message": "you do not have permissions to edit this page",
            },
        )

    if request.method == "POST":
        instance = Responsibility(person=person)
        data = ResponsibilityForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")
    table_data = Responsibility.objects.filter(person__id=person_id)
    form = ResponsibilityForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "Responsibility"}
    return render(request, template_name="showTable.html", context=data)


def show_award(request, person_id):
    user = request.user
    person = DeptPerson.on_site.filter(user=user).first()
    if not person.id == person_id:
        return render(
            request,
            template_name="error.html",
            context={
                "code": 401,
                "message": "you do not have permissions to edit this page",
            },
        )

    if request.method == "POST":
        instance = Award(person=person)
        data = AwardForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")
    table_data = Award.objects.filter(person__id=person_id)
    form = AwardForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "Awards"}
    return render(request, template_name="showTable.html", context=data)


def edit_journal_pub(request, id):

    instance = JournalPublication.objects.filter(id=id).first()
    person_id = instance.person.id
    form = JournalPublicationForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
        data = JournalPublicationForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("journal", person_id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)


def edit_conf_pub(request, id):

    instance = ConferencePublication.objects.filter(id=id).first()
    person_id = instance.person.id
    form = ConferencePublicationForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
        data = ConferencePublicationForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("conf", person_id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)


def edit_book_pub(request, id):

    instance = BookPublication.objects.filter(id=id).first()
    person_id = instance.person.id
    form = BookPublicationForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
        data = BookPublicationForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("book", person_id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)


def edit_project(request, id):

    instance = Project.objects.filter(id=id).first()
    person_id = instance.person.id
    form = ProjectForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
        data = ProjectForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("projects", person_id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)


def edit_event(request, id):

    instance = Event.objects.filter(id=id).first()
    person_id = instance.person.id
    form = EventForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
        data = EventForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("events", person_id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)


def edit_affiliation(request, id):

    instance = Affilation.objects.filter(id=id).first()
    person_id = instance.person.id
    form = AffilationForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
        data = AffilationForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("affiliation", person_id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)


def edit_phd(request, id):

    instance = PhDSupervised.objects.filter(id=id).first()
    person_id = instance.person.id
    form = PhDSupervisedForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
        data = PhDSupervisedForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("phd", person_id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)


def edit_pgd(request, id):

    instance = PGDissertationGuided.objects.filter(id=id).first()
    person_id = instance.person.id
    form = PGDissertationGuidedForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
        data = PGDissertationGuidedForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("pgd", person_id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)


def edit_patent(request, id):

    instance = Patent.objects.filter(id=id).first()
    person_id = instance.person.id
    form = PatentForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
            return redirect("patent", person_id)

        data = PatentForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("patent", person_id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)


def edit_responsibility(request, id):

    instance = Responsibility.objects.filter(id=id).first()
    person_id = instance.person.id
    form = ResponsibilityForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
        data = ResponsibilityForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("responsibility", person_id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)


def edit_award(request, id):

    instance = Award.objects.filter(id=id).first()
    person_id = instance.person.id
    form = AwardForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
        data = AwardForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("award", person_id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)


def add_profile_link(request):
    user = request.user
    person = DeptPerson.on_site.filter(user=user).first()
    if request.method == "POST":
        data = ProfileLinksForm(request.POST, instance=person)
        if data.is_valid():
            messages.success(request, "Saved")
        else:
            messages.error(request, f"failed to save, {data.errors}")
        return redirect("edit_profile", person.id)
    else:
        return render(
            request,
            template_name="error.html",
            context={
                "code": 401,
                "message": "you do not have permissions to edit this page",
            },
        )


def add_research_info(request):
    user = request.user
    person = DeptPerson.on_site.filter(user=user).first()
    if request.method == "POST":
        data = ResearchInfoForm(request.POST, instance=person)
        if data.is_valid():
            messages.success(request, "Saved")
        else:
            messages.error(request, f"failed to save, {data.errors}")
        return redirect("edit_profile", person.id)
    else:
        return render(
            request,
            template_name="error.html",
            context={
                "code": 401,
                "message": "you do not have permissions to edit this page",
            },
        )


def edit_profile_links(request, id):

    instance = ProfileLinks.objects.filter(id=id).first()
    person_id = instance.person.id
    form = ProfileLinksForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
        data = ProfileLinksForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("edit_profile", person_id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)


def edit_research_info(request, id):

    instance = ResearchInfo.objects.filter(id=id).first()
    person_id = instance.person.id
    form = ResearchInfoForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
        data = ResearchInfoForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("edit_profile", person_id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)

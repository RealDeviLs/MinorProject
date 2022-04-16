from django.contrib import messages
from django.shortcuts import get_object_or_404, render

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

    profile_links = ProfileLinks.objects.filter(person=person).all()
    profile_link_form = ProfileLinksForm()
    data = {
        "person": person,
        "form": basic_form,
        "profile_links": profile_links,
        "profile_link_form": profile_link_form,
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
            messages.error(request, "failed to save please contact support")

    table_data = JournalPublication.objects.filter(person__id=person_id)

    form = JournalPublicationForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "Conference"}
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
            messages.error(request, "failed to save please contact support")

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
            messages.error(request, "failed to save please contact support")

    table_data = BookPublication.objects.filter(person__id=person_id)
    form = BookPublicationForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "Conference"}
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
            messages.error(request, "failed to save please contact support")

    table_data = Project.objects.filter(personperson__id=person_id)
    form = ProjectForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "Conference"}
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
            messages.error(request, "failed to save please contact support")

    table_data = Event.objects.filter(person__id=person_id)
    form = EventForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "Conference"}
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
            messages.error(request, "failed to save please contact support")
    table_data = Affilation.objects.filter(person__id=person_id)
    form = AffilationForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "Conference"}
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
            messages.error(request, "failed to save please contact support")

    table_data = PhDSupervised.objects.filter(person__id=person_id)
    form = PhDSupervisedForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "Conference"}
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
            messages.error(request, "failed to save please contact support")
    table_data = PGDissertationGuided.objects.filter(person__id=person_id)
    form = PGDissertationGuidedForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "Conference"}
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
            messages.error(request, "failed to save please contact support")

    table_data = Patent.objects.filter(person__id=person_id)
    form = PatentForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "Conference"}
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
            messages.error(request, "failed to save please contact support")
    table_data = Responsibility.objects.filter(person__person__id=person_id)
    form = ResponsibilityForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "Conference"}
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
            messages.error(request, "failed to save please contact support")
    table_data = Award.objects.filter(person__id=person_id)
    form = AwardForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "Conference"}
    return render(request, template_name="showTable.html", context=data)

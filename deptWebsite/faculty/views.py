from django.shortcuts import get_object_or_404, render

from .forms import BasicProfileForm
from .models import DeptPerson

# Create your views here.


def faculty_page(request):
    faculty = DeptPerson.on_site.all()
    data = {"faculty": faculty}
    return render(request, template_name="faculty_page.html", context=data)


def faculty_detail(request, id):
    profile = get_object_or_404(DeptPerson, id=id)
    profile_links = profile.profile_links.content
    research_info = profile.research_info.content
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

    user = request.user
    person = DeptPerson.on_site.filter(user=user).first()
    if person is not None:
        form = BasicProfileForm(instance=person)
    else:
        form = BasicProfileForm()

    data = {"form": form}
    return render(request, template_name="edit_basic.html", context=data)

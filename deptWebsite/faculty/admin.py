import re
from django.contrib import admin
from .models import (
    DeptPerson,
    ResearchInfo,
    ProfileLinks,
    JournalPublication,
    ConferencePublication,
    BookPublication,
    Project,
    Event,
    Affilation,
    PhDSupervised,
    PGDissertationGuided,
    Patent,
    Responsibility,
    Award,
)

# Register your models here.


class ResearchInfoInline(admin.StackedInline):
    model = ResearchInfo

class ProfileLinksInline(admin.StackedInline):
    model = ProfileLinks

class JournalPublicationInline(admin.StackedInline):
    model = JournalPublication

class ConferencePublicationInline(admin.StackedInline):
    model = ConferencePublication

class BookPublicationInline(admin.StackedInline):
    model = BookPublication

class ProjectInline(admin.StackedInline):
    model = Project


class EventInline(admin.StackedInline):
    model = Event


class AffilationInline(admin.StackedInline):
    model = Affilation


class PhDSupervisedInline(admin.StackedInline):
    model = PhDSupervised

class PGDissertationGuidedInline(admin.StackedInline):
    model = PGDissertationGuided

class PatentInline(admin.StackedInline):
    model = Patent


class ResponsibilityInline(admin.StackedInline):
    model = Responsibility


class AwardInline(admin.StackedInline):
    model = Award


@admin.register(DeptPerson)
class DeptPersonAdmin(admin.ModelAdmin):
    inlines = [
        ResearchInfoInline,
        ProfileLinksInline,
        JournalPublicationInline,
        ConferencePublicationInline,
        BookPublicationInline,
        ProjectInline,
        EventInline,
        AffilationInline,
        PhDSupervisedInline,
        PGDissertationGuidedInline,
        PatentInline,
        ResponsibilityInline,
        AwardInline,
    ]
    class Meta:
        model = DeptPerson

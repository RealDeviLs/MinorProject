import re
from turtle import mode
from django.contrib import admin
from .models import (
    DeptPerson,
    ResearchInterests,
    Publication,
    Project,
    Event,
    Affilation,
    Scholar,
    Patent,
    Responsibility,
    Award,
)

# Register your models here.


class ResearchInterestsInline(admin.StackedInline):
    model = ResearchInterests


class PublicationInline(admin.StackedInline):
    model = Publication


class ProjectInline(admin.StackedInline):
    model = Project


class EventInline(admin.StackedInline):
    model = Event


class AffilationInline(admin.StackedInline):
    model = Affilation


class ScholarInline(admin.StackedInline):
    model = Scholar


class PatentInline(admin.StackedInline):
    model = Patent


class ResponsibilityInline(admin.StackedInline):
    model = Responsibility


class AwardInline(admin.StackedInline):
    model = Award


@admin.register(DeptPerson)
class DeptPersonAdmin(admin.ModelAdmin):
    inlines = [
        ResearchInterestsInline,
        PublicationInline,
        EventInline,
        AffilationInline,
        ScholarInline,
        PatentInline,
        ResponsibilityInline,
        AwardInline,
    ]
    class Meta:
        model = DeptPerson

from django import forms
from django.forms import Textarea

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


class BasicProfileForm(forms.ModelForm):
    class Meta:
        model = DeptPerson
        exclude = ("id", "user", "dept_edit_access", "on_site", "department")
        widgets = {
            "address": Textarea(attrs={"rows": 1}),
            "qualification": Textarea(attrs={"rows": 1}),
        }


class ProfileLinksForm(forms.ModelForm):
    class Meta:
        model = ProfileLinks
        exclude = ["person"]


class ResearchInfoForm(forms.ModelForm):
    class Meta:
        model = ResearchInfo
        exclude = ["person"]
        widgets = {
            "content": Textarea(attrs={"rows": 1}),
        }


class JournalPublicationForm(forms.ModelForm):
    class Meta:
        model = JournalPublication
        exclude = ["person"]
        widgets = {
            "description": Textarea(attrs={"rows": 1}),
        }


class ConferencePublicationForm(forms.ModelForm):
    class Meta:
        model = ConferencePublication
        exclude = ["person"]
        widgets = {
            "description": Textarea(attrs={"rows": 1}),
        }


class BookPublicationForm(forms.ModelForm):
    class Meta:
        model = BookPublication
        exclude = ["person"]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ["person"]
        widgets = {
            "date_start": forms.DateInput(
                format=("%d-%m-%Y"),
                attrs={
                    "class": "myDateClass",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
            "date_end": forms.DateInput(
                format=("%d-%m-%Y"),
                attrs={
                    "class": "myDateClass",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ["person"]


class AffilationForm(forms.ModelForm):
    class Meta:
        model = Affilation
        exclude = ["person"]


class PhDSupervisedForm(forms.ModelForm):
    class Meta:
        model = PhDSupervised
        exclude = ["person"]


class PGDissertationGuidedForm(forms.ModelForm):
    class Meta:
        model = PGDissertationGuided
        exclude = ["person"]


class PatentForm(forms.ModelForm):
    class Meta:
        model = Patent
        exclude = ["person"]
        widgets = {
            "date": forms.DateInput(
                format=("%d-%m-%Y"),
                attrs={
                    "class": "myDateClass",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
        }


class ResponsibilityForm(forms.ModelForm):
    class Meta:
        model = Responsibility
        exclude = ["person"]
        widgets = {
            "date_start": forms.DateInput(
                format=("%d-%m-%Y"),
                attrs={
                    "class": "myDateClass",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
            "date_end": forms.DateInput(
                format=("%d-%m-%Y"),
                attrs={
                    "class": "myDateClass",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
        }


class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        exclude = ["person"]

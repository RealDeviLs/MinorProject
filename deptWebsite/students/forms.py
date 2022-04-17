from django import forms
from django.forms import Textarea

from .models import Internship, Placement, Project, Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ("department", "on_site")
        widgets = {"department_description": Textarea(attrs={"rows": 5})}


class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        exclude = ("person",)


class PlacementForm(forms.ModelForm):
    class Meta:
        model = Placement
        exclude = ("person",)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ("person",)

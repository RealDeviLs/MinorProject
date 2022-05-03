from django import forms
from django.forms import Textarea

from .models import AcademicProgram


class AcademicProgramForm(forms.ModelForm):
    class Meta:
        model = AcademicProgram
        exclude = ("department", "on_site")
        widgets = {"department_description": Textarea(attrs={"rows": 2})}


# class ProgramPeoForm(forms.ModelForm):
#     class Meta:
#         model = ProgramPeo
#         exclude = ("academic_program",)
#         widgets = {"department_description": Textarea(attrs={"rows": 2})}

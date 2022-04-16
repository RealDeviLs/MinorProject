from django import forms

from .models import DeptPerson


class BasicProfileForm(forms.ModelForm):
    class Meta:
        model = DeptPerson
        exclude = ("id", "user", "dept_edit_access", "on_site", "department")

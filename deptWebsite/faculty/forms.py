from django import forms

from .models import DeptPerson


class BasicProfileForm(forms.ModelForm):
    class Meta:
        model = DeptPerson
        exclude = ["department", "on_site", "dept_edit_access", "user"]

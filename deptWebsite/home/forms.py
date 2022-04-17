from django import forms
from django.forms import Textarea

from .models import DeptNews


class DeptNewsForm(forms.ModelForm):
    class Meta:
        model = DeptNews
        exclude = (
            "department",
            "on_site",
        )
        widgets = {
            "description": Textarea(attrs={"rows": 1}),
        }

from django import forms
from django.forms import Textarea

from .models import DeptNews


class DateInput(forms.DateInput):
    input_type = "date"


class DeptNewsForm(forms.ModelForm):
    class Meta:
        model = DeptNews
        exclude = (
            "department",
            "on_site",
        )
        widgets = {
            "description": Textarea(attrs={"rows": 1}),
            "date_end": forms.DateInput(
                format=("%d-%m-%Y"),
                attrs={
                    "class": "myDateClass",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
        }

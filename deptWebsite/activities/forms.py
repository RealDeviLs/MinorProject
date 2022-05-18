from django import forms

from .models import Activity, ActivityImage


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        exclude = ("department", "on_site")
        widgets = {
            "date_from": forms.DateInput(
                format=("%d-%m-%Y"),
                attrs={
                    "class": "myDateClass",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
            "date_to": forms.DateInput(
                format=("%d-%m-%Y"),
                attrs={
                    "class": "myDateClass",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
        }


class ActivityImageForm(forms.ModelForm):
    class Meta:
        model = ActivityImage
        exclude = ("activity",)

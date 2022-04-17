from django import forms
from django.forms import Textarea
from faculty.models import DeptPerson

from .models import SocietyClub, WhiteLabel


class WhiteLabelForm(forms.ModelForm):
    hod = forms.ModelChoiceField(queryset=None)

    class Meta:
        model = WhiteLabel
        exclude = (
            "department",
            "on_site",
        )
        widgets = {
            "department_description": Textarea(attrs={"rows": 1}),
            "vision": Textarea(attrs={"rows": 1}),
            "misison": Textarea(attrs={"rows": 1}),
            "hod_message": Textarea(attrs={"rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["hod"].queryset = DeptPerson.on_site.all()
        self.fields["hod"].initial = WhiteLabel.on_site.first().hod


class SocietyClubForm(forms.ModelForm):
    class Meta:
        model = SocietyClub
        exclude = ("dept",)
        widgets = {
            "description": Textarea(attrs={"rows": 1}),
        }

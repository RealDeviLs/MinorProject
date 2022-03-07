import imp
from django import forms
from .models import WhiteLabel, SocietyClub, HeroPhotos
from django.forms import CharField,Textarea,TextInput


class WhiteLabelForm(forms.ModelForm):

    class Meta:
        model = WhiteLabel
        exclude = ('department',"on_site")
        widgets = {
            "department_description":Textarea(attrs={'cols':22, 'rows': 5})
        }
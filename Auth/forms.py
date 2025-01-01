from django.forms import ModelForm
from .models import RegistrationLink
from django import forms


class RegistrationLinkForm(ModelForm):
    class Meta:
        model = RegistrationLink
        fields = ['email', 'department']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3'}),
            'department': forms.Select(attrs={'class': 'form-control mb-3'})
        }
from django.forms import ModelForm
from .models import SupportDocument
from django import forms

class SupportDocumentForm(ModelForm):
    class Meta:
        model = SupportDocument
        fields = ['name', 'file']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control mb-3'}),
        }
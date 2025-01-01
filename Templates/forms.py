from django.forms import ModelForm
from .models import Template
from django import forms

class TemplateForm(ModelForm):
    class Meta:
        model = Template
        fields = ['name', 'file']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'file': forms.FileInput(attrs={'class': 'form-control mb-3'})
        }
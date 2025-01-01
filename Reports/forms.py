from django.forms import ModelForm
from django import forms
from .models import Report


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['report_type', 'file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'class': 'form-control mb-3'}),
            'report_type': forms.Select(attrs={'class': 'form-control mb-3'})
        }
from django.forms import ModelForm
from django import forms
from .models import Appointment

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'location', 'notes', 'person_name', 'person_email', 'person_contact']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control mb-3', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control mb-3', 'type': 'time'}),
            'location': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'notes': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'person_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'person_email': forms.EmailInput(attrs={'class': 'form-control mb-3'}),
            'person_contact': forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }
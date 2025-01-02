from django.forms import ModelForm
from .models import Case
from django.forms import widgets


class CaseForm(ModelForm):
    class Meta:
        model = Case
        exclude = ('comment', 'pictures', 'paid', 'fee_note', 'reference_number', 'reports', 'status', 'support_documents')
        widgets = {
            'date_reported': widgets.DateInput(attrs={'class': 'form-control mb-3', 'type': 'date'}),
            'insurance_Company': widgets.Select(attrs={'class': 'form-control mb-3'}),
            'company_email': widgets.EmailInput(attrs={'class': 'form-control mb-3'}),
            'policy': widgets.Select(attrs={'class': 'form-control mb-3'}),
            'client': widgets.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': widgets.Textarea(attrs={'class': 'form-control  mb-3'}),
            'reference_number': widgets.TextInput(attrs={'class': 'form-control mb-3'}),
            'assessor': widgets.Select(attrs={'class': 'form-control mb-3'}),
        }
        labels = {
            'date_reported': 'Date Reported',
            'insurance_Company': 'Insurance Company',
            'company_email': 'Company Email',
            'policy': 'Policy',
            'client': 'Client',
            'description': 'Description',
            'reference_number': 'Reference Number',
            'status': 'Status',
            'assessor': 'Assessor',
        }


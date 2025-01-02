from django.forms import ModelForm
from .models import FeeNote
from django.forms import widgets

class FeeNoteForm(ModelForm):
    class Meta:
        model = FeeNote
        fields = ['case', 'currency', 'inspection_and_assessment_fee', 'accommodation_fee', 'out_of_office_allowance', 'travel_and_assessment_fee', 'photos']
        widgets = {
            'case': widgets.Select(attrs={'class': 'form-control mb-3'}),
            'currency': widgets.Select(attrs={'class': 'form-control mb-3'}),
            'inspection_and_assessment_fee': widgets.NumberInput(attrs={'class': 'form-control mb-3'}),
            'accommodation_fee': widgets.NumberInput(attrs={'class': 'form-control mb-3'}),
            'out_of_office_allowance': widgets.NumberInput(attrs={'class': 'form-control mb-3'}),
            'travel_and_assessment_fee': widgets.NumberInput(attrs={'class': 'form-control mb-3'}),
            'photos': widgets.NumberInput(attrs={'class': 'form-control mb-3'}),
        }
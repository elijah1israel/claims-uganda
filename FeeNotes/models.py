from django.db import models

statuses = [('Unpaid', 'Unpaid'), ('Paid', 'Paid')]

class FeeNote(models.Model):
    case = models.OneToOneField('Cases.Case', on_delete=models.SET_NULL, null=True, related_name='_feenote_case')
    inspection_and_assessment_fee = models.DecimalField(max_digits=10, decimal_places=2)
    accommodation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    out_of_office_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    travel_and_assessment_fee = models.DecimalField(max_digits=10, decimal_places=2)
    photos = models.DecimalField(max_digits=10, decimal_places=2)
    value_added_tax = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    valid_fee_note = models.FileField(upload_to='FeeNotes/files', null=True)
    last_reminder = models.DateTimeField(null=True)
    status = models.CharField(max_length=50, choices=statuses, default='Unpaid')
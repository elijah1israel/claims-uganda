from django.db import models

class Assessor(models.Model):
    staff = models.OneToOneField('Staff.Staff', on_delete=models.SET_NULL, null=True)
    cases = models.ManyToManyField('Cases.Case', blank=True, related_name='assessor_cases')
    reports = models.ManyToManyField('Reports.Report', blank=True, related_name='assessor_reports')
    fee_notes = models.ManyToManyField('FeeNotes.FeeNote', blank=True, related_name='assessor_fee_notes')
    
    
    def __str__(self):
        return self.staff.user.first_name + ' ' + self.staff.user.last_name
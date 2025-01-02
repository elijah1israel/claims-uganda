from django.db import models
from django.utils.timezone import now


insurance_companies = (
    ('MUA', 'MUA Insurance (U) LTD'),
    ('MF', 'Mayfair Insurance Uganda LTD'),
    ('UAP', 'Old Mutual Insurance Uganda LTD'),
    ('JIC', 'Jubilee Alliance General Insurance Company'),
    ('BIC', 'Britam Insurance Company'),
    ('EXCEL', 'Excel Insurance Company LTD'),
    ('APA', 'APA Insurance (U) LTD'),
    ('AL', 'Alliance Africa General Insurance LTD'),
    ('LG', 'Liberty General Insurance (U) LTD'),
    ('GA', 'GA Insurance Uganda'),
    ('ICEA', 'ICEA Lion General Insurance LTD')
)

insurance_policies = (
    ('IAR', 'Industrial All Risks Insurance Policy'),
    ('GIT', 'Marine Goods in Transit Insurance Policy'),
    ('FR', 'Fire & Allied Peril Insurance Policy'),
    ('FMD', 'Fire Material Damage Policy'),
    ('CAR', "Contractor's All Risk Insurance"),
    ('MT', 'Commercial Motor Policy')
    
)

statuses = (
    ('Pending', 'Pending'),
    ('In Progress', 'In Progress'),
    ('Closed', 'Closed'),
)

class Case(models.Model):
    insurance_Company = models.CharField(max_length=50, choices=insurance_companies, default='Not Selected')
    company_email = models.EmailField(null=True)
    policy = models.CharField(max_length=50, choices=insurance_policies)
    date_reported = models.DateField(default=now)
    client = models.CharField(max_length=50)
    description = models.TextField()
    comment = models.TextField(null=True)
    pictures = models.ManyToManyField('Pictures.Picture', blank=True, related_name='case_pictures')
    reference_number = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=statuses, default='Pending')
    reports = models.ManyToManyField('Reports.Report', blank=True, related_name='case_reports')
    assessor = models.ForeignKey('Assessors.Assessor', on_delete=models.SET_NULL, null=True, related_name='_case_assessor')
    fee_note = models.OneToOneField('FeeNotes.FeeNote', on_delete=models.SET_NULL, null=True, related_name='case_feenote')
    support_documents = models.ManyToManyField('SupportDocuments.SupportDocument', blank=True, related_name='case_support_documents')
    field_notes = models.FileField(upload_to='CaseFieldNotes/files', null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.reference_number

    def edit_form(self):
        from .forms import CaseForm
        return CaseForm(instance=self)
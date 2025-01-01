from django.db import models
from django.utils.timezone import now

report_types = (
    ('Preliminary', 'Preliminary'),
    ('Addendum', 'Addendum'),
    ('Final', 'Final')
)

statuses = (
    ('In Progress', 'In Progress'),
    ('Submitted', 'Submitted'),
)
               
class  Report(models.Model):
    date_uploaded = models.DateTimeField(default=now)
    case = models.ForeignKey('Cases.Case', on_delete=models.SET_NULL, null=True)
    report_type = models.CharField(max_length=50, choices=report_types, default='Not Selected')
    file = models.FileField(upload_to='Reports/files')
    status  = models.CharField(max_length=50, choices=statuses, default='In Progress')
    submissions = models.ManyToManyField('Submissions.Submission', related_name='report_submissions')
    
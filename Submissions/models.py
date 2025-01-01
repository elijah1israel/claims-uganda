from django.db import models
from django.utils.timezone import now

class Submission(models.Model):
    date = models.DateTimeField(default=now)
    report = models.OneToOneField('Reports.Report', on_delete=models.CASCADE)
    comments = models.ManyToManyField('Comments.Comment')

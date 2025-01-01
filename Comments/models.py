from django.db import models
from django.utils.timezone import now

class Comment(models.Model):
    date = models.DateTimeField(default=now)
    report = models.ForeignKey('Reports.Report', models.CASCADE)
    author = models.ForeignKey('Staff.Staff', models.CASCADE)
    text = models.TextField()

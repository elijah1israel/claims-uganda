from django.db import models
from django.utils.timezone import now

frequencies = (
    ('Daily', 'Daily'),
    ('Weekly', 'Weekly'),
    ('Monthly', 'Monthly')
)

statuses = (
    ('Running', 'Running'),
    ('Paused', 'Paused'),
    ('Stopped', 'Stopped')
)

class Reminder(models.Model):
    created_at = models.DateTimeField(default=now)
    frequency = models.CharField(choices=frequencies, null=True, max_length=100)
    last_sent = models.DateTimeField(null=True)
    run_until = models.DateTimeField(null=True)
    status = models.CharField(max_length=100, choices=statuses)
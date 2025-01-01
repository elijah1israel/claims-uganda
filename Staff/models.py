from django.db import models
from django.contrib.auth.models import User
from Cases.models import Case

departments = (
    ('Finance', 'Finance'),
    ('Assessors', 'Assessors'),
    ('Administration', 'Administration')
)

statuses = (
    ('Active', 'Active'),
    ('Inactive', 'Inactive')
)

class Staff(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    api_key = models.UUIDField(null=True)
    profile_picture = models.ImageField(upload_to='Staff/profile_pictures/', null=True, blank=True)
    department = models.CharField(max_length=100, choices=departments)
    status = models.CharField(max_length=100, choices=statuses, default='Active')
    appointments = models.ManyToManyField('Appointments.Appointment', blank=True, related_name='assessor_appointments')

    def __str__(self):
        return self.user.first_name+' '+self.user.last_name
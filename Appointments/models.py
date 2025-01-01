from django.db import models

class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    notes = models.TextField()
    person_name = models.CharField(max_length=100)
    person_email = models.EmailField()
    person_contact = models.CharField(max_length=20)
    staff = models.ForeignKey('Staff.Staff', on_delete=models.CASCADE)
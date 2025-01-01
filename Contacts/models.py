from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
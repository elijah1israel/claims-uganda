from django.db import models
from uuid import uuid4
from Staff.models import departments

class RegistrationLink(models.Model):
    email = models.EmailField()
    department = models.CharField(max_length=100, choices=departments, null=True)
    token = models.UUIDField(unique=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return self.email


class ResetPasswordLink(models.Model):
    email = models.EmailField()
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    token = models.UUIDField(unique=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return self.email
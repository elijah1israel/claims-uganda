from django.db import models

class Notification(models.Model):
    staff = models.ForeignKey('Staff.Staff', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    action_url = models.URLField()
    button_text = models.CharField(max_length=100, null=True)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

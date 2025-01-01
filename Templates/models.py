from django.db import models

class Template(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='Templates/files')
    downloads = models.IntegerField(default=0)

    def __str__(self):
        return self.name
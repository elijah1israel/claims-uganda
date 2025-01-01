from django.db import models

class Picture(models.Model):
    case = models.ForeignKey('Cases.case', on_delete=models.SET_NULL, null=True, related_name='case_pictures')
    image = models.ImageField(upload_to='Pictures/files')
    caption = models.CharField(max_length=50, null=True)
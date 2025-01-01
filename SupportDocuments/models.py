from django.db import models
from django.utils.timezone import now

class SupportDocument(models.Model):
    case = models.ForeignKey('Cases.case', on_delete=models.CASCADE)
    date_uploaded = models.DateField(default=now)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='SupportDocuments/files')

    def __str__(self):
        return self.name

    def document_type(self):
        if self.file.name.endswith('.pdf'):
            return 'PDF'
        elif self.file.name.endswith('.doc') or self.file.name.endswith('.docx'):
            return 'Word'
        elif self.file.name.endswith('.jpg') or self.file.name.endswith('.png'):
            return 'Image'
        else:
            return 'Other'
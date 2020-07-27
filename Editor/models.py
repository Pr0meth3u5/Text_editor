#not using
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
 
class Efield(models.Model):
    Rollno = models.CharField(max_length=50 , null=True)
    content = RichTextUploadingField(blank=True)

class TeachId(models.Model):
    teachId = models.CharField(max_length=10, null=True)
    mail = models.CharField(max_length=50, null=True)
    def __str__(self) -> str:
        return self.teachId + "_" + self.mail


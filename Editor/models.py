from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
 
class Efield(models.Model):
    Rollno = models.CharField(max_length=200 , null=True)
    content = RichTextUploadingField(blank=True)


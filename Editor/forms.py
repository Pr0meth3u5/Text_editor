from .models import Efield
from django import forms
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class Efield_form(forms.Form):
    Rollno = forms.CharField(max_length=50)
    TeachId = forms.CharField(max_length=10)
    content = forms.CharField(widget=CKEditorUploadingWidget(), label=False)
    """class Meta:
        model = Efield
        fields = ['content']"""
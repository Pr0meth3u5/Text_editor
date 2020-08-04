from django.contrib import admin
from django.db import models
from .models import Efield, TeachId

admin.site.register(Efield)
class TeachIdAdmin(admin.ModelAdmin):
    list_display = ('Name','mail','teachId')

admin.site.register(TeachId, TeachIdAdmin)
# Register your models here.

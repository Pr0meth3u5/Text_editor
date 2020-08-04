from django.urls import path
from ckeditor_uploader import views as uploader_views
from . import views
app_name = 'Editor'
urlpatterns = [
    
    path('', views.Home, name='Home'),
    path('ajax/check_Teachid', views.Validate_Tid, name="Validate_Tid"),
]
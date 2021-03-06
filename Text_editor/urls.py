"""Text_editor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.conf.urls.static import static
from django.conf import settings
from ckeditor_uploader import views as ck_views
from django.contrib.auth.decorators import login_required
#from .views import test

urlpatterns = [
    #path('polls/',include('polls.urls')),
    #path("new", test ),
    path('admin/', admin.site.urls),
    path('Editor/', include('Editor.urls')),
    path('Editor/ckeditor/upload', ck_views.upload, name='ckeditor_upload'),
    path('Editor/ckeditor/browse', login_required(ck_views.browse), name='ckeditor_browse'),
   # path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, 
           document_root=settings.MEDIA_ROOT)
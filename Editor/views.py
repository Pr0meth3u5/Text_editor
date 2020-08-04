import pdfkit
from django.contrib import messages
from django.shortcuts import render
from .forms import Efield_form
from .models import TeachId
from django.http import HttpResponse, JsonResponse
from .utils import renderToPdf, sendMail

def Home(request):
    if request.method == "POST":
        Post_form = Efield_form(request.POST)
        if Post_form.is_valid:
            data = request.POST.copy()
            Tid = data.get("TeachId")
            if not TeachId.objects.filter(teachId=Tid).exists():
                return HttpResponse("Inavlid TeacherId")
            
            Tmail = TeachId.objects.get(teachId=Tid).mail
            Assignment = data.get("content")
            Roll = data.get("Rollno")
            Assignment = Assignment.replace('src="/', 'src="D:/Local_Projects/Django_Text/Text_editor/')
            Pdfpath = renderToPdf(Assignment, Tid, Roll)
            sendMail(Pdfpath, Tmail)
            return HttpResponse(Pdfpath, Tmail)

    field = Efield_form()
    return render(request, "editor.html", {"field": field})

def Validate_Tid(request):
    if request.method == "GET":
        Tid = request.GET.get('TeachId', None)

        data = {
            'is_Valid': TeachId.objects.filter(teachId=Tid).exists(),
            'Name': TeachId.objects.get(teachId=Tid).Name if TeachId.objects.filter(teachId=Tid).exists() else "None"
        }
        return JsonResponse(data)
    



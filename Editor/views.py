import pdfkit
from django.contrib import messages
from django.shortcuts import render
from .forms import Efield_form
from django.http import HttpResponse
from .utils import renderToPdf, sendMail


def Home(request):
    if request.method == "POST":
        Post_form = Efield_form(request.POST)
        if Post_form.is_valid:
            data = request.POST.copy()
            Assignment = data.get("content")
            # Roll = data.get("Rollno")
            Assignment = Assignment.replace('src="/', 'src="D:/Local_Projects/Django_Text/Text_editor/')
            Pdfpath = renderToPdf(Assignment)
            sendMail(Pdfpath)
            return HttpResponse(Pdfpath)

    field = Efield_form()
    return render(request, "editor.html", {"field": field})


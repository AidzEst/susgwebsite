from django.shortcuts import render
from reportlab.pdfgen import canvas
import io
from django.http import FileResponse
from django.http import HttpResponse

#Executive
def exec_header(request):
    return render(request, 'Executive/exec_header.html')

def exec_home(request):
    return render(request, 'Executive/exec_home.html')

def constitution(request):
    return render(request, 'Executive/constitution.html')

def chairpersons(request):
    return render(request, 'Executive/chairpersons.html')
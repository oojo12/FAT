from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'py2tableau/home.html')

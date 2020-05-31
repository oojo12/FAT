from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'py2tableau/home.html')


def update_user_db(request):
    if request.method == "POST":
        user = User(Fname=fname, Lname=lname)
        user.save()
    else:
        return HttpResponse(User.objects.all())

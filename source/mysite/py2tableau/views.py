from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
def home(request):
    return HttpResponse("This is the home page")

def update_user_db(request):
    form = UserForm(None)
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        "form": form
        }

    return render(request, 'py2tableau/update_user.html', context)

def check_user_db(request):
    return HttpResponse(User.objects.all())

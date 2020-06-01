from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
import pandas as pd
import pickle

def home(request):
    return render(request, 'py2tableau/home.html')

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

def datasets(request):
    return render(request, 'py2tableau/datasets.html')

### this can be copied and pasted for new dashboards. Any addition to this should be added to the urls.py file.
def dashboards(request):
    return render(request, 'py2tableau/dashboards.html')

def infer(request):
    form = ModelForm(None)
    if request.method == "POST":
        form = ModelForm(request.POST)
        model_data = pd.from_dict(form.cleaned_data)
        mdl = pickle.load(r'..\models\model.sav')
        pred = mdl.predict(model_data)
        context = {
            "form": form
            }
        print(pred)
    return render(request, 'py2tableau/infer_model_data.html', context)

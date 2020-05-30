from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('py2tableau/home.html')
    return HttpResponse("Hello, world. You're at the polls index.")

from django import forms
from .models import *

class UserForm(forms.Form):
    fname = forms.CharField()
    lname = forms.CharField()


class ModelForm(forms.Form):
    pass

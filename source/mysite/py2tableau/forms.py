from django import forms
from .models import *

class UserForm(forms.Form):
    fname = forms.CharField()
    lname = forms.CharField()


class ModelForm(forms.Form):
    ### this can be updated with the fields that should be used for the model
    ### the applicable field types can be found here https://docs.djangoproject.com/en/3.0/ref/forms/fields/
    ### be sure to name the var what the dataset variable name is expected to be for the
    ### model
    pass

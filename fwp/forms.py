from django import forms
from .models import *

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'

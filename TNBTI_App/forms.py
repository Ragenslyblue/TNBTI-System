from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = RegisterUser
        fields = '__all__'



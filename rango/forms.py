from django import forms
from django.contrib.auth.models import User

from rango.models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

class EMessageForm(forms.ModelForm):
    class Meta:
        model = EMessage
        exclude = ('author', )

class Meta:
    model = User
    fields = ('username', 'email', 'password')

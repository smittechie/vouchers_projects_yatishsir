from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from . import models
from .models import Employee
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    # name = forms.CharField(max_length=30, required=True)
    email = forms.EmailInput()
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password' ]


class LogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    # class Meta:
    #     model = Employee
    #     fields = ['email','username', 'password']

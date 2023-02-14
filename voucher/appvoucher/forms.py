from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from . import models
from .models import Employee


class SignUpForm(forms.Form):
    email = forms.EmailInput()
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['email', 'password']


class LogInForm(forms.Form):
    email = forms.EmailInput()

    class Meta:
        model = Employee
        fields = ['email', 'password']

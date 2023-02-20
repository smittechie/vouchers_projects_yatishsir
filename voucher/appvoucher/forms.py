from django.forms import ModelForm, Select
from django import forms
from django.contrib.auth.models import User
from . import models
from .models import Employee, Voucher
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password

# class SignUpForm(forms.ModelForm):
#     email = forms.EmailInput()
#     password = forms.PasswordInput()
#
#     class Meta:
#         model = User
#         fields = ['name']


'''old one form which created the user not the model employee '''


class SignUpForm(forms.ModelForm):
    # name = forms.CharField(max_length=30, required=True)
    # email = forms.EmailInput()
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())

    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ['username', 'email', 'password']


''' Not recommended to save password here and is instance is giving email id od current user '''


# def save(self, commit=False):
#     instance = super().save(commit=True)
#     print(instance)
#     instance.password = make_password(instance.password)
#     if commit:
#         instance.save()
#     return instance


class LogInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    # class Meta:
    #     model = Employee
    #     fields = ['email','username', 'password']


class Voucherallotment_to_id_Form(forms.ModelForm):
    # voucher = forms.ModelChoiceField(queryset=Voucher.objects.all())
    voucher = forms.ModelMultipleChoiceField(
        queryset=Voucher.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Employee

        fields = [
            "voucher",
        ]

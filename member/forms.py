from django import forms
from models import Member
from django.contrib.auth.models import User


class UserCreationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password')


class MemberCreationForm(forms.ModelForm):
    class Meta:
        model=Member
        fields=('phone_number','address')
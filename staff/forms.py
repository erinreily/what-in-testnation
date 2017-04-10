from django import forms
from models import Staff
from django.contrib.auth.models import User


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class StaffCreationForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('wage', 'title', 'supervisor')

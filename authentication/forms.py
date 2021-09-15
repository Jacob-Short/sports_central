from authentication.models import SportsUser
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)
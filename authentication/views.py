from django.shortcuts import render,HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from authentication.forms import CreateUserForm, LoginForm
from authentication.models import SportsUser
from django.views.generic import View
import re


def index_view(request):
    context = {}
    return render(request, 'index.html', context)


class LoginView(View):
    '''logginig in as registered user'''
    def get(self, request):
        template_name = "generic_form.html"
        form = LoginForm()
        return render(request, template_name, {"form": form, "header": "Login"})


    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data.get("username"), password=data.get("password")
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))


class SignUpView(View):
    '''creating a new user'''
    def get(self, request):
        template_name = "generic_form.html"
        form = CreateUserForm()
        return render(request, template_name, {"form": form, "header": "Signup"})


    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = SportsUser.objects.create_user(
                username=data.get("username"),
                email=data.get("email"),
                password=data.get("password")
            )
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from accounts.forms import RegistrationForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("mag:home_view"))
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            human = True
            user = form.get_user() 
            if user is not None:
                messages.add_message(request, messages.SUCCESS, "you'r login was successful.")
                login(request, user)
                return HttpResponseRedirect(reverse("mag:blog_view"))
            else:
                messages.add_message(request, messages.ERROR, "please enter true credetioals.")
    else:
        form = LoginForm()
    return render(request, "accounts/auth/login.html",  {"form":form})

def registration_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("mag:home_view"))
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            human = True
            user = form.save()
            messages.add_message(request, messages.SUCCESS, "you'r registraion is successful ")
            return HttpResponseRedirect(reverse("mag:home_view"))
    else:
        form = RegistrationForm()
    return render(request, "accounts/auth/registration.html" , {"form":form})

@login_required()
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("mag:home_view"))


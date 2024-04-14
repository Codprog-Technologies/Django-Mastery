from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from users import forms


# Create your views here.

def login_view(request):
    if request.method == "POST":
        # 1. validate email + password valid -> authenticate
        # 2. if valid -> login -> login
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request=request, username=email, password=password)
        if user:
            login(request, user)
            return HttpResponse('Login successful')
        else:
            return HttpResponse('Invalid Username or Password')
    else:
        return render(request, "users/login.html")


def login_view_django_form(request):
    if request.method == "POST":
        # 1. validate email + password valid -> authenticate
        # 2. if valid -> login -> login
        form = forms.UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponse('Login successful')
        else:
            context = {
                "form": form
            }
            return render(request, "users/login_with_django_form.html", context)
    else:
        context = {
            "form": forms.UserAuthenticationForm()
        }
        return render(request, "users/login_with_django_form.html", context)


def signup(request):
    if request.method == "POST":
        form = forms.UserSignupForm(data=request.POST)
        if form.is_valid():
            # form.save()
            login(request, form.save())
            return HttpResponse('Signup Successful')
        else:
            context = {
                "form": form
            }
            return render(request, "users/signup.html", context)
    else:
        context = {
            "form": forms.UserSignupForm()
        }
        return render(request, "users/signup.html", context)
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from users import forms, models


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


def advocate_signup(request):
    if request.method == "POST":
        form = forms.AdvocateSignup(data=request.POST)
        advocate_profile_form = forms.AdvocateProfileForm(data=request.POST)
        if form.is_valid() and advocate_profile_form.is_valid():
            user = form.save()
            advocate_profile = advocate_profile_form.save(commit=False)
            advocate_profile.user = user
            advocate_profile.save()
            login(request, user)
            return HttpResponse('Signup Successful')
        else:
            context = {
                "form": form,
                "advocate_profile_form": advocate_profile_form
            }
    else:
        context = {
            "form": forms.AdvocateSignup(),
            "advocate_profile_form": forms.AdvocateProfileForm()
        }
    return render(request, "users/signup.html", context)


def client_signup(request):
    if request.method == "POST":
        form = forms.ClientSignup(data=request.POST)
        if form.is_valid():
            # form.save()
            login(request, form.save())
            return HttpResponse('Signup Successful')
        else:
            context = {
                "form": form
            }
    else:
        context = {
            "form": forms.ClientSignup()
        }
    return render(request, "users/signup.html", context)


def update_account(request):
    user = request.user
    if request.user.role == models.User.RoleChoices.ADVOCATE:
        is_adv = True
    else:
        is_adv = False
    if request.method == "POST":
        form = forms.UserUpdateForm(data=request.POST, instance=user)
        if is_adv:
            advocate_profile_form = forms.AdvocateProfileForm(data=request.POST, instance=request.user.advocate_profile)
            if form.is_valid() and advocate_profile_form.is_valid():
                form.save()
                advocate_profile_form.save()
        else:
            if form.is_valid():
                form.save()
        context = {
            "form": form,
            "advocate_profile_form": advocate_profile_form if is_adv else None
        }
    else:
        context = {
            "form": forms.UserUpdateForm(instance=user),
            "advocate_profile_form": forms.AdvocateProfileForm(instance=user.advocate_profile) if is_adv else None
        }
    return render(request, "users/update_profile.html", context)

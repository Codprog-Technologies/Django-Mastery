from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView, ListView

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
            next = ""
            if request.GET:
                next = request.GET["next"]
            if next:
                return HttpResponseRedirect(next)
            return redirect("home")
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


@require_http_methods(["POST"])
def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect("home")


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


@transaction.atomic
def advocate_signup(request):
    if request.method == "POST":
        form = forms.AdvocateSignup(data=request.POST)
        advocate_profile_form = forms.AdvocateProfileForm(data=request.POST)
        phone_number_form = forms.PhoneNumberForm(data=request.POST)
        if form.is_valid() and advocate_profile_form.is_valid() and phone_number_form.is_valid():
            user = form.save()
            # raise Exception()
            advocate_profile = advocate_profile_form.save(commit=False)
            advocate_profile.user = user
            advocate_profile.save()
            advocate_profile_form.save_m2m()
            phone_number = phone_number_form.save(commit=False)
            phone_number.user = user
            phone_number.save()
            login(request, user)
            return HttpResponse('Signup Successful')
        else:
            context = {
                "form": form,
                "advocate_profile_form": advocate_profile_form,
                "phone_number_form": phone_number_form
            }
    else:
        context = {
            "form": forms.AdvocateSignup(),
            "advocate_profile_form": forms.AdvocateProfileForm(),
            "phone_number_form": forms.PhoneNumberForm()
        }
    return render(request, "users/signup.html", context)


def client_signup(request):
    if request.method == "POST":
        form = forms.ClientSignup(data=request.POST)
        phone_number_form = forms.PhoneNumberForm(data=request.POST)
        if form.is_valid() and phone_number_form.is_valid():
            user = form.save()
            phone_number = phone_number_form.save(commit=False)
            phone_number.user = user
            phone_number.save()
            permission = Permission.objects.get(codename="view_platformreview")
            user.user_permissions.add(permission)
            permission = Permission.objects.get(codename="add_platformreview")
            user.user_permissions.add(permission)
            login(request, user)
            return HttpResponse('Signup Successful')
        else:
            context = {
                "form": form,
                "phone_number_form": phone_number_form
            }
    else:
        context = {
            "form": forms.ClientSignup(),
            "phone_number_form": forms.PhoneNumberForm()
        }
    return render(request, "users/signup.html", context)


@login_required
def update_account(request):
    user = request.user
    phone_numbers = user.phone_number_set.all().order_by("id")
    if request.user.role == models.User.RoleChoices.ADVOCATE:
        is_adv = True
    else:
        is_adv = False
    if request.method == "POST":
        form = forms.UserUpdateForm(data=request.POST, instance=user)
        phone_number_form1 = forms.PhoneNumberForm(data=request.POST,
                                                   label_suffix=" 1", prefix="1",
                                                   instance=phone_numbers[0] if phone_numbers else None)
        phone_number_form2 = forms.PhoneNumberOptionalForm(data=request.POST,
                                                           label_suffix=" 2", prefix="2",
                                                           instance=phone_numbers[1] if len(
                                                               phone_numbers) > 1 else None)
        if is_adv:
            advocate_profile_form = forms.AdvocateProfileForm(data=request.POST, instance=request.user.advocate_profile)
            if form.is_valid() and advocate_profile_form.is_valid() and phone_number_form1.is_valid() and \
                    (not phone_number_form2.has_changed() or phone_number_form2.is_valid()):
                form.save()
                phone_number = phone_number_form1.save(commit=False)
                phone_number.user = user
                phone_number.save()
                advocate_profile_form.save()
                if phone_number_form2.has_changed():
                    phone_number2 = phone_number_form2.save(commit=False)
                    phone_number2.user = user
                    phone_number2.save()
                messages.success(request, "Your profile was updated.")
        else:
            if form.is_valid() and phone_number_form1.is_valid() and \
                    (not phone_number_form2.has_changed() or phone_number_form2.is_valid()):
                form.save()
                phone_number_form1.save()
                if phone_number_form2.has_changed():
                    phone_number2 = phone_number_form2.save(commit=False)
                    phone_number2.user = user
                    phone_number2.save()
                messages.success(request, "Your profile was updated.")
        context = {
            "form": form,
            "advocate_profile_form": advocate_profile_form if is_adv else None,
            "phone_number_form1": phone_number_form1,
            "phone_number_form2": phone_number_form2
        }
    else:
        context = {
            "form": forms.UserUpdateForm(instance=user),
            "advocate_profile_form": forms.AdvocateProfileForm(instance=user.advocate_profile) if is_adv else None,
            "phone_number_form1": forms.PhoneNumberForm(instance=phone_numbers[0] if phone_numbers else None,
                                                        label_suffix=" 1", prefix="1"),
            "phone_number_form2": forms.PhoneNumberOptionalForm(
                instance=phone_numbers[1] if len(phone_numbers) > 1 else None,
                label_suffix=" 2", prefix="2")
        }
    return render(request, "users/update_profile.html", context)


class AdvocateDetailView(DetailView):
    template_name = "users/advocate_details.html"
    model = models.User
    context_object_name = "advocate_user"

    def get_queryset(self):
        return super().get_queryset().filter(role=models.User.RoleChoices.ADVOCATE)


class AdvocateListView(ListView):
    template_name = "users/advocate_list.html"
    # model = models.User
    queryset = models.User.objects.filter(role=models.User.RoleChoices.ADVOCATE)
    context_object_name = "advocate_list"
    paginate_by = 4

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render


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

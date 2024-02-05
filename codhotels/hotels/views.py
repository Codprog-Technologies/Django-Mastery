from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def test_func(request):
    return HttpResponse("TEST")


def html_view(request):
    return HttpResponse("<h1> This is Heading </h1>")


def template_view(request):
    return render(request, "hotels/template.html")


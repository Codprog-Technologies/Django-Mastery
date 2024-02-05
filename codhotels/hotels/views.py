from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def test_func(request):
    return HttpResponse("TEST")


def html_view(request):
    return HttpResponse("<h1> This is Heading </h1>")


def template_view(request):
    context = {
        'name': 'John Doe',
        'user': {
            'first_name': 'john',
            'last_name': 'doe'
        }
    }
    return render(request, "hotels/template.html", context)


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
        },
        'hotels': [
            {
                'name': 'Taj',
                'address': 'Mumbai, India'
            },
            {
                'name': 'Sapphire',
                'address': 'Banglore, India'
            },
            {
                'name': 'Heritage',
                'address': 'Ahmedabad, India'
            },
            {
                'name': 'Lotus',
                'address': 'Delhi, India'
            }
        ]
    }
    return render(request, "hotels/template.html", context)


def home(request):
    return render(request, "hotels/home.html")


def about_us(request):
    return render(request, "hotels/about.html")


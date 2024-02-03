from django.http import HttpResponse


# Create your views here.

def test_func(request):
    return HttpResponse("TEST")

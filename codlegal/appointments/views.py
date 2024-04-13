from django.http import HttpResponse
from django.shortcuts import render

from appointments import models, forms


# Create your views here.

def home(request):
    context = {
        'practice_areas': models.PracticeArea.objects.all()
    }
    return render(request, "appointments/home.html", context=context)


def about(request):
    return render(request, "appointments/about.html")


def practice_area(request):
    if request.method == "POST":
        form = forms.PracticeAreaForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Practice Area Created')
        else:
            context = {
                "form": form
            }
            return render(request, "appointments/practice_area.html", context)
    else:
        context = {
            "form": forms.PracticeAreaForm()
        }
        return render(request, "appointments/practice_area.html", context)

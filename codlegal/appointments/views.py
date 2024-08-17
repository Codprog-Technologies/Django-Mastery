from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

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


class PracticeAreaView(CreateView):
    template_name = "appointments/practice_area.html"
    form_class = forms.PracticeAreaForm

    def get_success_url(self):
        return self.request.get_full_path()


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, TemplateView, ListView, DeleteView

from appointments import models, forms
from users.models import User


# Create your views here.

def home(request):
    context = {
        'practice_areas': models.PracticeArea.objects.all()
    }
    return render(request, "appointments/home.html", context=context)


class HomePage(TemplateView):
    template_name = "appointments/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['practice_areas'] = models.PracticeArea.objects.all()
        return context


def about(request):
    return render(request, "appointments/about.html")


class AboutPage(TemplateView):
    template_name = "appointments/about.html"


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


class AppointmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = models.Appointment
    fields = ["advocate", "start_at"]
    success_message = "Appointment was created Successfully"

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)


class UpcomingAppointmentListView(LoginRequiredMixin, ListView):
    model = models.Appointment
    paginate_by = 4
    ordering = ["start_at"]

    def get_queryset(self):
        queryset = super().get_queryset()
        logged_in_user = self.request.user
        if logged_in_user.role == User.RoleChoices.CLIENT:
            return queryset.filter(client=logged_in_user, start_at__gt=timezone.now())
        elif logged_in_user.role == User.RoleChoices.ADVOCATE:
            return queryset.filter(advocate=logged_in_user, start_at__gt=timezone.now())
        return queryset.none()


class AppointmentDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = models.Appointment
    success_url = reverse_lazy("appointment_list")
    success_message = "Appointment Deleted Successfully"

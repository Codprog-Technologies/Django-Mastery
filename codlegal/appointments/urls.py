from django.urls import path

from appointments import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("about/", views.AboutPage.as_view(), name="about"),
    path("practice-area/", views.PracticeAreaView.as_view(), name="practice_area"),
    path("appointments/book/", views.AppointmentCreateView.as_view(), name="appointment_create"),
]
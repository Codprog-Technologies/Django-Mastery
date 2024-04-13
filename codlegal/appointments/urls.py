from django.urls import path

from appointments import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("practice-area/", views.practice_area, name="practice_area"),
]
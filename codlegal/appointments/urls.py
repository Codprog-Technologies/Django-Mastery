from django.urls import path

from appointments import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("practice-area/", views.PracticeAreaView.as_view(), name="practice_area"),
]
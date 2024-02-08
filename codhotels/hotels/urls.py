from django.urls import path

from hotels import views

urlpatterns = [
    path("test/", views.test_func),
    path("html/", views.html_view),
    path("list/", views.template_view, name="hotels_list"),
    path("home/", views.home, name="home"),
    path("about/", views.about_us, name="about"),
]
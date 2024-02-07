from django.urls import path

from hotels import views

urlpatterns = [
    path("test/", views.test_func),
    path("html/", views.html_view),
    path("template/", views.template_view),
    path("home/", views.home),
    path("about/", views.about_us),
]
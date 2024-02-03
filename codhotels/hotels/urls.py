from django.urls import path

from hotels import views

urlpatterns = [
    path("test/", views.test_func)
]
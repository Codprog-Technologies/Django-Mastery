from django.urls import path

from users import views

urlpatterns = [
    path("login/", views.login_view_django_form, name="login"),
    path("signup/", views.signup, name="signup"),
]
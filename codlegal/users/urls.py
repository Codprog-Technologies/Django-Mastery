from django.urls import path

from users import views

urlpatterns = [
    path("login/", views.login_view_django_form, name="login"),
    # path("signup/", views.signup, name="signup"),
    path("signup/advocate/", views.advocate_signup, name="advocate_signup"),
    path("signup/client/", views.client_signup, name="client_signup"),
    path("update/", views.update_account, name="update_account"),
]
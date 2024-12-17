from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.urls import path

from users import views
from users.views import CustomLoginView

urlpatterns = [
    path("login/", CustomLoginView.as_view(template_name="users/login_with_django_form.html"), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("password-change/", PasswordChangeView.as_view(template_name="users/password_change_form.html"), name="password_change"),
    path("password-change-done/", PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"), name="password_change_done"),
    path("password-reset/", PasswordResetView.as_view(template_name="users/password_reset_form.html"), name="password_reset"),
    path("password-reset-done/", PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<str:token>/", PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset-complete/", PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="password_reset_complete"),
    # path("signup/", views.signup, name="signup"),
    path("signup/advocate/", views.advocate_signup, name="advocate_signup"),
    path("signup/client/", views.client_signup, name="client_signup"),
    path("update/", views.update_account, name="update_account"),
    # path("advocates/<int:pk>/", views.AdvocateDetailView.as_view(), name="advocate_detail"),
    path("advocates/<int:pk>/", views.AdvocateDetailWithAppointmentFormView.as_view(), name="advocate_detail"),
    path("advocates/", views.AdvocateListView.as_view(), name="advocate_list"),
]
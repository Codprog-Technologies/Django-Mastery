from django.urls import path

from core import views

urlpatterns = [
    path("health/", views.HealthCheckView.as_view(), name="healthcheck")
]

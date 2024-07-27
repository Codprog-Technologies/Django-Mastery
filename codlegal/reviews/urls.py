from django.urls import path
from reviews import views

urlpatterns = [
    path("app/", views.submit_app_review, name="submit_app_review"),
    path("app/list", views.view_app_reviews, name="view_app_reviews"),
    path("app/update/<int:pk>", views.update_app_review, name="update_app_review"),
]
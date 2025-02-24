from django.urls import path

from users import views

urlpatterns = [
    path('', views.CreateUserView.as_view(), name="create_user"),
    path('<int:pk>/', views.DestroyUserView.as_view(), name="destroy_user")
]
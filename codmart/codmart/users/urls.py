from django.urls import path

from users import views

urlpatterns = [
    # path('', views.CreateUserView.as_view(), name="create_user"),
    path('', views.ListCreateUserView.as_view(), name="list_create_user"),
    # path('<int:pk>/', views.DestroyUserView.as_view(), name="destroy_user"),
    # path('<int:pk>/', views.UpdateUserView.as_view(), name="update_user")
    path('<int:pk>/', views.RetrieveUpdateDestroyUserView.as_view(), name="retrieve_update_destroy_user")
]
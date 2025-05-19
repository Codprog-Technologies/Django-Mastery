from dj_rest_auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

from users import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('', views.CreateUserView.as_view(), name="create_user"),
    path('', views.ListCreateUserView.as_view(), name="list_create_user"),
    # path('<int:pk>/', views.DestroyUserView.as_view(), name="destroy_user"),
    # path('<int:pk>/', views.UpdateUserView.as_view(), name="update_user")
    path('<int:pk>/', views.RetrieveUpdateDestroyUserView.as_view(), name="retrieve_update_destroy_user"),
    # path('token/', obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
]
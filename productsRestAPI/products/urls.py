from django.urls import path, include
from rest_framework.routers import SimpleRouter

from products import views

router = SimpleRouter()

router.register('products', views.ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]

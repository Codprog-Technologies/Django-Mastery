from django.urls import path, include
from rest_framework.routers import SimpleRouter

from products import views
from products.views import save_product_api_django_core

router = SimpleRouter()

router.register('products', views.ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
    path('django-create-product/', save_product_api_django_core, name="django-create-product")
]

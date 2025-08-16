from django.urls import path
from rest_framework import routers

from payments import views

router = routers.SimpleRouter()
router.register('orders', views.OrderViewSet, basename='order')

urlpatterns = [
                  path("webhooks/stripe/", views.StripeWebhookView.as_view(), name="stripe_webhooks")
              ] + router.urls

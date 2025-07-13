from rest_framework import routers

from payments import views

router = routers.SimpleRouter()
router.register('orders', views.OrderViewSet, basename='order')

urlpatterns = [] + router.urls

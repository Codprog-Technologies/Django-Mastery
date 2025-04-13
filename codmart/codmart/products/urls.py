from rest_framework.routers import SimpleRouter

from products import views

router = SimpleRouter()
router.register('', views.ProductViewSet, 'product')

urlpatterns = router.urls
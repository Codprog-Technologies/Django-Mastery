from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from products import models, serializers
from products.permissions import IsAdminUserOrReadOnly


# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):  # Or Inherit from GenericViewSet along with mixins

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [IsAdminUserOrReadOnly]

from rest_framework import viewsets

from products import models, serializers


# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):  # Or Inherit from GenericViewSet along with mixins

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

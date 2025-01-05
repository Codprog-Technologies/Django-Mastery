from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from products import models, serializers


# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductsSerializer
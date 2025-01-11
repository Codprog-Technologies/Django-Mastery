from django.core import serializers as django_serializers
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet

from products import models, serializers


# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductsSerializer


@csrf_exempt
def save_product_api_django_core(request):
    """
    Save Product Information ( Core Django )
    """
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    if request.META.get('CONTENT_TYPE') != 'application/json':
        return JsonResponse({'detail': 'Content-Type not supported'}, status=415)
    deserialized_data = django_serializers.deserialize('json', request.body)
    saved_instances = []
    for data in deserialized_data:
        data.save()
        saved_instances.append(data.object)
    return HttpResponse(django_serializers.serialize(
        'json', saved_instances,
        fields=['id', 'name', 'price']),
        content_type='application/json'
    )

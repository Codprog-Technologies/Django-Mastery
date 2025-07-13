from rest_framework import mixins, viewsets, permissions

from payments import models, serializers


# Create your views here.

class OrderViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = serializers.OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.Order.objects.filter(user=self.request.user)

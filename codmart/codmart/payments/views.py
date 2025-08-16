import stripe
from django.conf import settings
from rest_framework import mixins, viewsets, permissions, status, views
from rest_framework.response import Response

from payments import models, serializers

# Create your views here.

stripe.api_key = settings.STRIPE_API_KEY


class OrderViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = serializers.OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.Order.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client_secret = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_data = serializer.data
        if client_secret:
            response_data['client_secret'] = client_secret
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        # call stripe , if payment_channel -> ONLINE
        if serializer.validated_data['payment_channel'] == models.PaymentChannel.ONLINE:
            total_amount = int(serializer.validated_data['total_amount'] * 100)
            payment_intent = stripe.PaymentIntent.create(
                amount=total_amount,
                currency='inr',
                automatic_payment_methods={
                    'enabled': True,
                }
            )
            pg_id = payment_intent.id
            serializer.save(pg_id=pg_id)
            return payment_intent.client_secret
        else:
            serializer.save()


class StripeWebhookView(views.APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)
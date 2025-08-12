from rest_framework import serializers

from payments import models


class OrderCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Order
        fields = "__all__"
        read_only_fields = ('user', 'total_amount', 'status', 'pg_id', 'created_at', 'updated_at')
        extra_kwargs = {
            'product': {'required': True, 'allow_null': False},
            'address': {'required': True, 'allow_null': False}
        }


    def validate(self, attrs):
        product = attrs.get('product')
        gst_amount = (product.price * 18) / 100
        attrs['total_amount'] = product.price + gst_amount
        if attrs['payment_channel'] == models.PaymentChannel.ONLINE:
            attrs['status'] = models.OrderStatus.CREATED
        else:
            attrs['status'] = models.OrderStatus.CONFIRMED
        return attrs

    def create(self, validated_data):
        return super().create(validated_data)

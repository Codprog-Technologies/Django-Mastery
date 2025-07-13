from rest_framework import serializers

from payments import models


class OrderCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Order
        fields = "__all__"
        read_only_fields = ('user', 'total_amount', 'status', 'created_at', 'updated_at')

    def create(self, validated_data):
        product = validated_data.get('product')
        gst_amount = (product.price * 18) / 100
        validated_data['total_amount'] = product.price + gst_amount
        validated_data['status'] = models.OrderStatus.CONFIRMED
        return super().create(validated_data)

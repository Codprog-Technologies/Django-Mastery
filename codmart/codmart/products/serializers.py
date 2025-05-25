from rest_framework import serializers

from products import models


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = ('url', 'id')


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, source='productimage_set', required=True)

    class Meta:
        model = models.Product
        fields = '__all__'

    def create(self, validated_data):
        images = validated_data.pop('productimage_set')
        product = super().create(validated_data)
        for image in images:
            product.productimage_set.create(**image)
        return product

    def update(self, instance, validated_data):
        if 'productimage_set' in validated_data:
            images = validated_data.pop('productimage_set')
            instance.productimage_set.all().delete()
            for image in images:
                instance.productimage_set.create(**image)

        return super().update(instance, validated_data)

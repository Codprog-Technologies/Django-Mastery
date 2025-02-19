from django.core import validators
from rest_framework import serializers

from users import models


class UserSerializer(serializers.ModelSerializer):
    # first_name = serializers.CharField(max_length=150, required=True)
    class Meta:
        model = models.User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True, 'validators': [validators.MinLengthValidator(5)]},
            'first_name': {'required': True}
        }

    def validate_username(self, username):
        if username == 'test':
            raise serializers.ValidationError('This username is not allowed')
        return username.lower()

    def validate(self, attrs):
        first_name = attrs['first_name']
        password = attrs['password']
        if password.startswith(first_name):
            raise serializers.ValidationError('Password should not be similar to first_name')
        return attrs

    def create(self, validated_data):
        return models.User.objects.create_user(**validated_data)

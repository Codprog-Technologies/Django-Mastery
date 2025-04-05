from django.core import validators
from rest_framework import serializers

from users import models


class UserSerializer(serializers.ModelSerializer):
    # first_name = serializers.CharField(max_length=150, required=True)
    class Meta:
        model = models.User
        exclude = ('groups', 'user_permissions')
        extra_kwargs = {
            'password': {'write_only': True, 'validators': [validators.MinLengthValidator(5)]},
            'first_name': {'required': True},
            'role': {'required': True},
            'last_login': {'read_only': True},
            'date_joined': {'read_only': True},
            'is_staff': {'read_only': True},
            'is_active': {'read_only': True},
            'is_superuser': {'read_only': True},
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


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = ('groups', 'user_permissions', 'password')
        extra_kwargs = {
            'first_name': {'required': True},
            'role': {'required': True},
            'last_login': {'read_only': True},
            'date_joined': {'read_only': True},
            'is_staff': {'read_only': True},
            'is_active': {'read_only': True},
            'is_superuser': {'read_only': True},
            'username': {'read_only': True},
            'email': {'read_only': True},
        }

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
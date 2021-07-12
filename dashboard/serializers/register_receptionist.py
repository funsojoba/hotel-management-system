from rest_framework import serializers
from django.contrib.auth import get_user_model


class RegisterReceptionist(serializers.Serializer):
    first_name = serializers.CharField(trim_whitespace=True, max_length=50)
    last_name = serializers.CharField(trim_whitespace=True, max_length=50)
    phone = serializers.CharField(trim_whitespace=True, max_length=50)
    email = serializers.CharField(trim_whitespace=True, max_length=50)
    password = serializers.CharField(trim_whitespace=True, max_length=50)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'phone', 'password']
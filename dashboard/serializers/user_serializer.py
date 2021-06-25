from django.db.models import fields
from rest_framework import serializers

from dashboard.models.user import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True, style={"input_type":"password"})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'password']
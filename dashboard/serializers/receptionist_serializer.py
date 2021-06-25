from rest_framework import serializers
from dashboard.models.receptionist import Receptionist


class ReceptionistSerializer(serializers.ModelSerializer):
    avatar_url = serializers.FileField()

    class Meta:
        model = Receptionist
        fields = '__all__'
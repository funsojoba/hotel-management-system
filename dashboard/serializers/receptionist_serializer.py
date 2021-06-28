from rest_framework import serializers
from dashboard.models.receptionist import Receptionist


class ReceptionistSerializer(serializers.ModelSerializer):
    avatar_url = serializers.FileField()

    class Meta:
        model = Receptionist
        fields = ['avatar_url', 'user_id', 'gender',
                  'date_of_birth', 'state_of_origin', 'address']

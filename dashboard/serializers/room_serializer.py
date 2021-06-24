from django.db import models
from rest_framework import serializers
from dashboard.models.room import Room
from dashboard.models.room_status import RoomStatus
from dashboard.models.room_type import RoomType


class RoomStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomStatus
        fields = '__all__'


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'


class ListRoomSerializer(serializers.ModelSerializer):
    room_status = RoomStatusSerializer()
    room_type = RoomTypeSerializer()

    class Meta:
        model = Room
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.FileField(max_length=100000,
                                    allow_empty_file=False,
                                    use_url=True)
    )

    class Meta:
        model = Room
        fields = '__all__'

from rest_framework import generics
from db.models.room import Room
from db.serializers.room_serializer import RoomSerializer


class ListRooms(generics.ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

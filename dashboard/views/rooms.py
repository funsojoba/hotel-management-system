from django.shortcuts import render

from rest_framework import generics
from dashboard.models.room import Room
from dashboard.serializers.room_serializer import ListRoomSerializer, RoomSerializer


class ListRoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = ListRoomSerializer


class CreateRoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class GetRoomView(generics.RetrieveUpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

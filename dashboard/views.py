from django.shortcuts import render

from rest_framework import generics
from .models.room import Room
from .serializers.room_serializer import RoomSerializer


class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

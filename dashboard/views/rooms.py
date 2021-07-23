from decouple import config

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser

from dashboard.my_lib.response import Response
from dashboard.models.room import Room
from dashboard.serializers.room_serializer import ListRoomSerializer, RoomSerializer


import cloudinary.uploader


class ListRoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = ListRoomSerializer


class CreateRoomView(APIView):
    parser_classes = (MultiPartParser, JSONParser, FormParser)
    serializer_class = RoomSerializer

    def post(self, request):
        serializer = RoomSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(errors=dict(serializer.errors))

        if serializer.is_valid(raise_exception=True):
            images = serializer.validated_data['images']
            room_type = serializer.validated_data['room_type']
            room_status = serializer.validated_data['room_status']
            room_number = serializer.validated_data['room_number']
            price = serializer.validated_data['price']
            description = serializer.validated_data['description']

            img_url_list = []

            for image in images:
                upload_image = cloudinary.uploader.upload(
                    image, folder=config('IMG_FOLDER_NAME'))
                img_url_list.append(upload_image['url'])

            room = Room.objects.create(
                room_type=room_type, room_number=room_number, room_status=room_status, images=img_url_list, price=price, description=description)
            room.save()

            data = {}
            data['images'] = img_url_list
            data['created_at'] = room.created_at
            data['updated_at'] = room.updated_at

            response_data = {**{'Id': room.id}, **serializer.data, **data}
            return Response(data=dict(response_data), status=status.HTTP_201_CREATED)
        return Response(errors=dict(serializer.errors))


class GetRoomView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
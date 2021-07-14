from decouple import config
from django.utils.translation import override

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework import status, permissions

import cloudinary.uploader

from dashboard.lib.response import Response
from dashboard.models.receptionist import Receptionist
from dashboard.serializers.receptionist_serializer import ReceptionistSerializer


class ReceptionistView(APIView):
    serializer_class = ReceptionistSerializer
    queryset = Receptionist.objects.all()
    permission_classes = [permissions.IsAuthenticated]


    def post(self, request):
        data = request.data
        user_id = request.user.id

        serializer = self.serializer_class(data=data)
        data['user_id'] = user_id

        if not serializer.is_valid():
            return Response(errors=dict(serializer.errors), status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            avatar_url = serializer.validated_data['avatar_url']
            valid_extension = ['jpeg', 'jpg', 'png', 'svg', 'JPG', 'JPEG']

            if avatar_url.name.split('.')[-1] not in valid_extension:
                return Response(errors={"error": "invalid file format"}, status=status.HTTP_400_BAD_REQUEST)

            uploaded_image = cloudinary.uploader.upload(avatar_url, folder=config(
                'PROFILE_FOLDER_NAME'), user_filename=True, overwrite=True)
            image_url = uploaded_image.get('url')

            serializer.save(avatar_url=image_url)
            serializer_dict = dict(serializer.data)
            serializer_dict['avatar_url'] = image_url

            return Response(data=dict(serializer_dict))
        return Response(errors=dict(serializer.errors))

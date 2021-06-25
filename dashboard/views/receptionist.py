from decouple import config
from django.utils.translation import override

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework.response import Response
from rest_framework import status

import cloudinary.uploader

from dashboard.models.receptionist import Receptionist
from dashboard.serializers.receptionist_serializer import ReceptionistSerializer



class ReceptionistView(APIView):
    serializer_class = ReceptionistSerializer
    queryset = Receptionist.objects.all()

    def post(self, request):
        data = request.data
        data['user_id'] = request.user.id
        serializer = self.serializer_class(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            avatar_url = serializer.validated_data['avatar_url']
            valid_extension = ['jpeg', 'jpg', 'png', 'svg', 'JPG', 'JPEG']

            if avatar_url.name.split('.')[-1] not in valid_extension:
                return Response(data={"error": "invalid file format"})

            uploaded_image = cloudinary.uploader.upload(avatar_url, folder=config('PROFILE_FOLDER_NAME'), user_filename=True, overwritee=True)
            image_url = uploaded_image.get('url')
            
            serializer.save(avatar_url=image_url)
            serializer_dict = dict(serializer.data)
            serializer_dict['avatar_url'] = image_url

            print(serializer_dict)

            return Response(serializer_dict)
        return Response(serializer.errors)



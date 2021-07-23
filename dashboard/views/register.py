from django.contrib.auth import get_user_model
from rest_framework import status

from rest_framework.views import APIView

from dashboard.my_lib.response import Response
from dashboard.models.user import User
from dashboard.serializers.user_serializer import UserSerializer


class RegisterView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            first_name = serializer.data.get('first_name', '')
            last_name = serializer.data.get('last_name', '')
            phone = serializer.data.get('phone', '')
            email = serializer.data.get('email', '')
            password = serializer.data.get('password', '')

            user = get_user_model().objects.create(email=email, password=password, first_name=first_name,
                                                   last_name=last_name, phone=phone,)
            user.set_password(password)
            user.save()
            return Response(data=dict(serializer.data), status=status.HTTP_201_CREATED)

        return Response(errors=dict(serializer.errors), status=status.HTTP_400_BAD_REQUEST)

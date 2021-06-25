from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.views import APIView

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

            user = get_user_model().objects.create(first_name=first_name,
                                                   last_name=last_name, phone=phone, email=email, password=password)
            user.set_password(password)
            user.save()
            return Response(serializer.data)

        return Response(serializer.errors)

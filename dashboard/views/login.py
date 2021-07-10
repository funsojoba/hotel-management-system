from logging import error
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from dashboard.serializers.login import LoginSerializer
from dashboard.models.user import User
from dashboard.lib.response import Response


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        if not email or not password:
            return Response(data=None, errors={"Invalid credentials": "Ensure both email and password are correct"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=email, password=password)
        if not user:
            return Response(errors={"error":"user does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=user)
        return Response(errors=None, data={"Token": token.key}, status=status.HTTP_200_OK)
        

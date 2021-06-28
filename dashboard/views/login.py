from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from dashboard.serializers.login import LoginSerializer
from dashboard.models.user import User


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        db_email = User.objects.get(email=email)

        if not email or not password:
            return Response({"Invalid credentials": "Ensure both email and password are correct"}, status=status.HTTP_400_BAD_REQUEST)

        if db_email:
            print(db_email)
            return Response({"e choke":"db_email"})

        return Response({'onaga':'ko naga'})
        # serializer = self.serializer_class(user)
        # token, _ = Token.objects.get_or_create(user=user)
        # return Response({"Token": token.key}, status=status.HTTP_200_OK)

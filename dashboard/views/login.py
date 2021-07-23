from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

from dashboard.models.user import User
from dashboard.my_lib.response import Response
from dashboard.serializers.login import LoginSerializer


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        if not email or not password:
            return Response(data=None, errors={"Invalid credentials": "Ensure both email and password are correct"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()

        if not user:
            raise AuthenticationFailed("user not found")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")

        serializer = self.serializer_class(user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={"success": "login successfull", "token": token.key})

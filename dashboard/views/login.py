from django.contrib.auth.hashers import check_password
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

        user = authenticate(request, email=email, password=password)
        db_user = User.objects.filter(email=email)
        if db_user:
            db_user_password = db_user[0].password
            password_check = check_password(db_user_password, password)
            print(password_check)
        # db_password = check_password(password,)
        # if not user:
        #     return Response(errors={"error":"user does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        
        print(db_user[0].password, user)
        # token, _ = Token.objects.get_or_create(user=user)
        # return Response(data={"Token": token.key}, status=status.HTTP_200_OK)
        return Response({"Something":"db_user"})
        

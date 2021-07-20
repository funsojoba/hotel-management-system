import random
import string

from django.contrib.auth import get_user_model

from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import status

from dashboard.serializers.register_receptionist import RegisterReceptionist
from dashboard.lib.response import Response
from dashboard.models.receptionist import Receptionist
from dashboard.models.user import User


def create_otp():
    str_num = string.digits
    return ''.join(random.choice(str_num) for i in range(6))


class RegisterReceptionistView(APIView):
    serializer_class = RegisterReceptionist

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            first_name = serializer.data.get('first_name', '')
            last_name = serializer.data.get('last_name', '')
            email = serializer.data.get('email', '')
            password = serializer.data.get('password', '')
            phone = serializer.data.get('phone', '')

            db_email = User.objects.get(email=email)

            if db_email:
                return Response(errors={"error":"Email already exit"}, status=status.HTTP_400_BAD_REQUEST)

            user = get_user_model().objects.create(first_name=first_name,
                                                   last_name=last_name, phone=phone, email=email, password=password)
            
            user.set_password(password)
            user.otp_code = create_otp()
            user.is_active = True
            user.is_admin = True
            
            receptionist = Receptionist.objects.create(user_id=user)
            user.save()
            receptionist.save()

            return Response(data=dict(serializer.data), status=status.HTTP_201_CREATED)

        return Response(errors=dict(serializer.errors), status=status.HTTP_400_BAD_REQUEST)

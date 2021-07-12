from rest_framework.views import APIView
from rest_framework import status, permissions

from dashboard.models.booking import Booking
from dashboard.lib.response import Response
from dashboard.serializers.booking_serializer import BookingSerializer


class BookingView(APIView):
    serializer_class = BookingSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        data['user_id'] = request.user.id
        serializer = self.serializer_class(data=data)

        if not serializer.is_valid():
            return Response(errors=dict(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
            
        print(request)
        return Response(data=serializer)

        # user = data.get()
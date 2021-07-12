from rest_framework import serializers
from dashboard.models.booking import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['room_id', 'customer_id', 'payment_type', 'start_time',
                  'end_time', 'is_cancelled', 'created_at', 'updated_at']

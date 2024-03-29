import uuid

from django.db import models

from .room import Room
from .payment_type import PaymentType
from .user import User


class Booking(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    room_id = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.DO_NOTHING)
    start_time = models.DateField()
    end_time = models.DateField()
    is_cancelled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Booking for {self.customer_id.first_name}'

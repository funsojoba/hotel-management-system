import uuid

from django.db import models

from .room import Room
from .payment import Payment
from .user import User


class Reservation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)
    room_id = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(Payment, on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Reservation for {self.customer_id.first_name}'

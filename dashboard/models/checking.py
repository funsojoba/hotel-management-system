from django.db import models
import uuid

from .room import Room
from .user import User
from .booking import Booking


class Checking(models.Model):
    STATUS = (
        ('Check in', 'Check in'),
        ('Check out', 'Check out')
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    status = models.CharField(max_length=50, choices=STATUS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Check in for {self.user.first_name}'

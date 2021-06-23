import uuid

from django.db import models

from .room_status import RoomStatus
from .room_type import RoomType


class Room(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.DO_NOTHING)
    room_status = models.ForeignKey(RoomStatus, on_delete=models.DO_NOTHING)
    room_number = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Room {self.room_number}'

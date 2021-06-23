import uuid

from django.db import models


class RoomType(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)
    room_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.room_type

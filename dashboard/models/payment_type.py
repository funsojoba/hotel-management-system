import uuid

from django.db import models


class PaymentType(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

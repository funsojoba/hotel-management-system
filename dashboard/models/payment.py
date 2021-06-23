import uuid

from django.db import models

from .receptionist import Receptionist
from .user import User
from .payment_type import PaymentType


class Payment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.DO_NOTHING)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.amount

import uuid

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


class Receptionist(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('None-binary', 'None-binary'),
        ('Others', 'Others'),
        ('Rather not say', 'Rather not say')
    )

    User = get_user_model()
    AVATAR_URL = 'https://res.cloudinary.com/ddl2pf4qh/image/upload/v1623512852/24-248253_user-profile-default-image-png-clipart-png-download_qwj0qi.png'

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50, choices=GENDER)
    avatar_url = models.URLField(default=AVATAR_URL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

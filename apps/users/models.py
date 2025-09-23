from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('guest', 'GUEST'),
        ('barber', 'BARBER'),
        ('admin', 'ADMIN'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES,default='guest')
    photo = models.ImageField(upload_to='user_photos', null=True, blank=True)


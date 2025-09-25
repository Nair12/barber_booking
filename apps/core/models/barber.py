from django.db import models

from config import settings
from .barbers_point import BarbersPoint


class Barber(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="barber_profile",
        null=True,
    )
    id = models.BigAutoField(primary_key=True)

    exp = models.IntegerField()
    phone = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    pict_url = models.ImageField(upload_to="barbers")

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    point = models.ForeignKey(
        BarbersPoint,
        on_delete=models.SET_NULL,
        related_name="barbers",
        null=True

    )


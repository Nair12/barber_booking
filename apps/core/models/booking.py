from django.db import models
from .barber import Barber
from .barbers_point import BarbersPoint


class Booking(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_time = models.DateTimeField()
    user_phone = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    point = models.ForeignKey(
        BarbersPoint,
        on_delete=models.CASCADE,
        related_name="point"
    )

    barber = models.ForeignKey(
        Barber,
        on_delete=models.CASCADE,
        related_name="barber"
    )


    def __str__(self):
        return f"Booking {self.id} - {self.name}"

from django.db import models
from .barbers_point import BarbersPoint


class Barber(models.Model):
    id = models.BigAutoField(primary_key=True)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True, null=True)

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

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic or ''}".strip()

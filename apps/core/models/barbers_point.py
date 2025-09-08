from django.db import models


class BarbersPoint(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.address

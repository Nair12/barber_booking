from django.db import models


class Barber(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    exp = models.IntegerField()
    phone = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    pict_url = models.URLField()

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField()

    def __str__(self):
        return self.name

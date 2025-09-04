from django.db import models


class Booking(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    user_phone = models.CharField(max_length=20)
    name = models.CharField(max_length=100)


    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField()



    def __str__(self):
        return f"Booking {self.id} - {self.name}"

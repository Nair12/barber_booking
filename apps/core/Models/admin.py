from django.db import models


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField()

    def __str__(self):
        return self.name

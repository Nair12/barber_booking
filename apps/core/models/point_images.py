from django.db import models
from .barbers_point import BarbersPoint


class PointImages(models.Model):
    id = models.BigAutoField(primary_key=True)
    point_id = models.ForeignKey(
        BarbersPoint,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.URLField()




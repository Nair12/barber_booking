from django.db import models
from .barbers_point import BarbersPoint


class PointImages(models.Model):
    id = models.BigAutoField(primary_key=True)
    point_id = models.ForeignKey(
        BarbersPoint,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="point_images")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for point {self.point_id}"
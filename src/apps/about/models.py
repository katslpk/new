import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy
from storages.backends.s3boto3 import S3Boto3Storage

User = get_user_model()


class EngineType(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return f"{self.name}"


class CarInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_model = models.TextField()
    car_year = models.DecimalField(max_digits=4, decimal_places=0)
    start_mileage = models.DecimalField(max_digits=8, decimal_places=0)
    engine_volume = models.DecimalField(max_digits=2, decimal_places=1,)
    engine_type = models.ForeignKey(EngineType, on_delete=models.CASCADE)
    vin = models.TextField(unique=True, max_length=17)
    car_license_plate = models.TextField(unique=True)
    additional_info = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy("about:index_car", kwargs={"pk": str(self.pk)})

    def __str__(self):
        return f"{self.car_model} ({self.pk})"


class CarPhoto(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    car = models.ForeignKey(CarInfo, on_delete=models.CASCADE, related_name="img")
    original = models.FileField(storage=S3Boto3Storage())

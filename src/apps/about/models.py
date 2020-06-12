from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class CarInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    car_model = models.TextField(null=True, blank=True)
    car_year = models.DateField(null=True, blank=True)
    engine_volume = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    engine_type = models.TextField(null=True, blank=True)
    vin = models.TextField(max_length=17, unique=True, primary_key=True)
    car_license_plate = models.TextField(max_length=7, null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)

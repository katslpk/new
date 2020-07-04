from django.db import models

from apps.about.models import CarInfo


class Work(models.Model):
    car_model = models.ForeignKey(CarInfo, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    mileage = models.TextField(null=True, blank=True)
    type = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    cost = models.FloatField(null=True, blank=True)
    station = models.TextField(null=True, blank=True)

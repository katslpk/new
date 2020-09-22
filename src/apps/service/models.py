from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy

from apps.about.models import CarInfo

User = get_user_model()


class Type(models.Model):
    type = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type}"


class Station(models.Model):
    station = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.station}"


class Work(models.Model):
    car_model = models.ForeignKey(CarInfo, on_delete=models.CASCADE)
    date = models.DateField()
    mileage = models.TextField()
    type_of_work = models.ForeignKey(Type, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    cost = models.FloatField()
    station = models.ForeignKey(Station, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse_lazy("service:index", kwargs={"pk": str(self.pk)})

    def __str__(self):
        return f"{self.car_model} ({self.pk})"

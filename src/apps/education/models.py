from django.db import models


class Station(models.Model):
    name = models.TextField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"#{self.pk}:{self.name!r}"


class Work(models.Model):
    date = models.DateField(null=True, blank=True)
    mileage = models.TextField(null=True, blank=True)
    type = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    cost = models.FloatField(null=True, blank=True)
    station = models.ManyToManyField(Station, related_name="work")


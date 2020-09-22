from django.db import models

from apps.about.models import EngineType


class PriceLiter(models.Model):
    engine_type = models.ForeignKey(EngineType, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()

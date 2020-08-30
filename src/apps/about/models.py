from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy

User = get_user_model()


class CarInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_model = models.TextField(null=True, blank=True)
    car_year = models.DecimalField (null=True, blank=True, max_digits=4, decimal_places=0)
    engine_volume = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True
    )
    engine_type = models.TextField(null=True, blank=True)
    vin = models.TextField(max_length=17, null=True, blank=True)
    car_license_plate = models.TextField(null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy("about:index_car", kwargs={"pk": str(self.pk)})

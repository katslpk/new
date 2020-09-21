import uuid

import django.db.models.deletion
import storages.backends.s3boto3
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CarInfo",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("car_model", models.TextField()),
                ("car_year", models.DecimalField(decimal_places=0, max_digits=4)),
                ("start_mileage", models.DecimalField(decimal_places=0, max_digits=8)),
                ("engine_volume", models.DecimalField(decimal_places=1, max_digits=2)),
                ("vin", models.TextField(max_length=17, unique=True)),
                ("car_license_plate", models.TextField(unique=True)),
                ("additional_info", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="EngineType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="CarPhoto",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "original",
                    models.FileField(
                        storage=storages.backends.s3boto3.S3Boto3Storage(), upload_to=""
                    ),
                ),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="img",
                        to="about.CarInfo",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="carinfo",
            name="engine_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="about.EngineType"
            ),
        ),
        migrations.AddField(
            model_name="carinfo",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]

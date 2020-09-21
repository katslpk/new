import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("about", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PriceLiter",
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
                ("cost", models.DecimalField(decimal_places=2, max_digits=12)),
                ("date", models.DateField()),
                (
                    "engine_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="about.EngineType",
                    ),
                ),
            ],
        ),
    ]

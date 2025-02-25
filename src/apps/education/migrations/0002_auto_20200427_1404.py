# Generated by Django 3.0.5 on 2020-04-27 11:04

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("education", "0001_squashed_0006_auto_20200427_1004"),
    ]

    operations = [
        migrations.CreateModel(
            name="Work",
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
                ("date", models.DateField(blank=True, null=True)),
                ("mileage", models.TextField(blank=True, null=True)),
                ("type", models.TextField(blank=True, null=True)),
                ("comment", models.TextField(blank=True, null=True)),
                ("cost", models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(model_name="skills", name="degree",),
        migrations.RenameModel(old_name="Degree", new_name="Station",),
        migrations.DeleteModel(name="Education",),
        migrations.DeleteModel(name="Skills",),
        migrations.AddField(
            model_name="work",
            name="station",
            field=models.ManyToManyField(related_name="work", to="education.Station"),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-27 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [
        ("education", "0001_initial"),
        ("education", "0002_responsibility"),
        ("education", "0003_auto_20200423_2226"),
        ("education", "0004_auto_20200423_2235"),
        ("education", "0005_skills_name"),
        ("education", "0006_auto_20200427_1004"),
    ]

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Degree",
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
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Education",
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
                ("started_at", models.DateField(blank=True, null=True)),
                ("finished_at", models.DateField(blank=True, null=True)),
                ("name", models.TextField(blank=True, null=True)),
                ("summary", models.TextField(blank=True, null=True)),
                (
                    "degree",
                    models.ManyToManyField(
                        related_name="education", to="education.Degree"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Skills",
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
                ("summary", models.TextField()),
                (
                    "degree",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="skills",
                        to="education.Education",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-24 17:36

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("education", "0004_auto_20200423_2235"),
    ]

    operations = [
        migrations.AddField(
            model_name="skills",
            name="name",
            field=models.TextField(blank=True, null=True),
        ),
    ]

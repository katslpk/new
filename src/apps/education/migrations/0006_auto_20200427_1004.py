# Generated by Django 3.0.5 on 2020-04-27 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("education", "0005_skills_name"),
    ]

    operations = [
        migrations.RemoveField(model_name="skills", name="name",),
        migrations.AlterField(
            model_name="skills",
            name="degree",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="skills",
                to="education.Education",
            ),
        ),
    ]

# Generated by Django 3.0.7 on 2020-08-30 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('mileage', models.TextField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('cost', models.FloatField(blank=True, null=True)),
                ('station', models.TextField(blank=True, null=True)),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.CarInfo')),
            ],
        ),
    ]

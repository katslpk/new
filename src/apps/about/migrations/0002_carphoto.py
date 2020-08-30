# Generated by Django 3.0.7 on 2020-08-30 07:55

from django.db import migrations, models
import django.db.models.deletion
import storages.backends.s3boto3
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarPhoto',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('original', models.FileField(storage=storages.backends.s3boto3.S3Boto3Storage(), upload_to='')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='img', to='about.CarInfo')),
            ],
        ),
    ]

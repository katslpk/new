import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy
from storages.backends.s3boto3 import S3Boto3Storage

User = get_user_model()


class Post(models.Model):
    title = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy("blog:post", kwargs={"pk": str(self.pk)})


class Photo(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="photos")
    original = models.FileField(storage=S3Boto3Storage())

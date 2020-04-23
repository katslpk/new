from django.db import models


class Degree(models.Model):
    name = models.TextField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"#{self.pk}:{self.name!r}"


class Education(models.Model):
    started_at = models.DateField(null=True, blank=True)
    finished_at = models.DateField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    degree = models.ManyToManyField(Degree, related_name="education")


class Skills(models.Model):
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name="skills")
    summary = models.TextField()

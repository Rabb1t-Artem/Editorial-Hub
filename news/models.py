from django.conf import settings
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    content = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    topic = models.ManyToManyField(
        Topic,
        related_name="newspapers"
    )
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="newspapers",
    )

    def __str__(self):
        return self.title

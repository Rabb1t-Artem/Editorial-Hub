from django.conf import settings
from django.db import models
from django_resized import ResizedImageField


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ResizedImageField(
        size=[1080, 1080],
        upload_to='news_images/',
        crop=False,
        quality=75,
        force_format='WEBP',
        help_text='Будьте уважні, зображення буде масштабовано автоматично'
    )
    topics = models.ManyToManyField(
        Topic,
        related_name="newspapers"
    )
    redactor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="newspapers"
    )
    
    class Meta:
        ordering = ["-updated_at", "-created_at"]

    def __str__(self):
        return self.title

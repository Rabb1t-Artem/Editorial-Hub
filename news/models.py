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
        crop=['middle', 'center'],
        quality=75,
        force_format='JPEG',
        help_text='Рекомендований розмір 1080x1080 пікселів'
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

    def __str__(self):
        return self.title

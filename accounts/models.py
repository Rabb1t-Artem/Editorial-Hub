from django.contrib.auth.models import AbstractUser
from django.db import models
from django_resized import ResizedImageField


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    profile_image = ResizedImageField(
        size=[512, 512],
        upload_to='profile_images/',
        crop=['middle', 'center'],
        quality=75,
        force_format='WEBP',
        default='profile_images/no-avatar.png',
        blank=True
    )
    
    class Meta:
        db_table = "redactors"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    full_name = models.CharField(max_length=150, blank=True)
    info = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    gender_choices = [('M', 'Мужской'), ('F', 'Женский'), ('O', 'Другой')]
    gender = models.CharField(max_length=1, choices=gender_choices, blank=True)

    posts_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)
    followers_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username





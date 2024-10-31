from django.db import models
from django.contrib.auth.models import User

from apps.services.users.utils import dir_for_user


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    avatar = models.ImageField(upload_to=dir_for_user)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

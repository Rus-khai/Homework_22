from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватар')
    phone = models.CharField(max_length=25, verbose_name='Телефон', blank=True)
    country = models.CharField(max_length=50, verbose_name='Страна', blank=True)

    token = models.CharField(max_length=255, verbose_name='Токен активации', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

        def __str__(self):
            return self.email

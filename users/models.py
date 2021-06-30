from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username

    def get_absolute_url(self):
        return "login"

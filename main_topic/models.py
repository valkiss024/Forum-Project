from django.db import models
from django.urls import reverse


class MainTopic(models.Model):
    title = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=256, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("main-topic-list")

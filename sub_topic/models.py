import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone

from main_topic.models import MainTopic


class SubTopic(models.Model):
    title = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=256, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    main_topic = models.ForeignKey(MainTopic, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("sub-topic-list", kwargs={"pk": self.main_topic.id})

    def is_new(self):
        return self.date > timezone.now() - datetime.timedelta(minutes=30)

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from PIL import Image

from sub_topic.models import SubTopic


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    sub_topic = models.ForeignKey(SubTopic, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-list", kwargs={"pk": self.sub_topic.main_topic.id, "pk_sub": self.sub_topic.id})

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """Overwriting the save method to be able to resize the image before it is saved"""
        super().save(force_insert, force_update, using, update_fields)
        if self.image:
            img = Image.open(self.image.path)
            thumbnail_size = (540, 400)
            img.thumbnail(thumbnail_size)
            img.save(self.image.path)

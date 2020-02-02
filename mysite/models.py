from django.conf import settings
from django.db import models
from django.utils import timezone


class Prop(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='img/',default='img')  # これが重要
    def __str__(self):
        return self.title
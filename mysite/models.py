from django.conf import settings
from django.db import models
from django.utils import timezone



class Prop(models.Model):
    tit = models.CharField(max_length=200,default='title')
    head = models.TextField(default='def')
    text = models.TextField()
    img = models.ImageField(upload_to='img/',default='img')  # これが重要
    def __str__(self):
        return self.tit

class Prop_cal(models.Model):
    tit = models.CharField(max_length=200,default='title')
    head = models.TextField(default='def')
    text = models.TextField()
    img = models.ImageField(upload_to='img/',default='img')  # これが重要
    def __str__(self):
        return self.tit

class Prop_liner(models.Model):
    tit = models.CharField(max_length=200,default='title')
    head = models.TextField(default='def')
    text = models.TextField()
    img = models.ImageField(upload_to='img/',default='img')  # これが重要
    def __str__(self):
        return self.tit

class Prop_mine(models.Model):
    tit = models.CharField(max_length=200,default='title')
    head = models.TextField(default='def')
    text = models.TextField()
    img = models.ImageField(upload_to='img/',default='img')  # これが重要
    def __str__(self):
        return self.tit

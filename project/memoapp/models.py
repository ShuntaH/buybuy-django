from django.db import models
from django.utils import timezone


# Create your models here.


class Day(models.Model):
    title = models.CharField('title', max_length=200)
    text = models.TextField('memo', blank=True)
    date = models.DateTimeField('created', default=timezone.now)

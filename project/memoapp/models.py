from django.db import models
from django.utils import timezone


# Create your models here.


class Day(models.Model):
    title = models.CharField('Want ...', max_length=200)
    text = models.TextField('Description', blank=True)
    date = models.DateTimeField('When you hit it on...', default=timezone.now)

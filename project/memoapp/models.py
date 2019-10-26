from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Day(models.Model):
    title = models.CharField("What's on your mind?", max_length=200)
    text = models.TextField('Notes', blank=True)
    date = models.DateTimeField('When you hit it on...', default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

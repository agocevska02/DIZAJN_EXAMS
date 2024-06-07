from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    poster = models.ImageField(upload_to='events/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isOpen = models.BooleanField(default=False)
    bends = models.CharField(max_length=100)
    participants = models.IntegerField(default=0)


class Bend(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    year = models.IntegerField()
    num = models.IntegerField(default=0)


class BendEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    bend = models.ForeignKey(Bend, on_delete=models.CASCADE)

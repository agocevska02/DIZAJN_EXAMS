from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class WorkSpace(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    fixOldTimer = models.BooleanField()


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)



class Automobile(models.Model):
    type = models.CharField(max_length=50)
    manifacture = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    max_speed = models.IntegerField()
    color = models.CharField(max_length=50)


class ManufactureWorkSpace(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    workspace = models.ForeignKey(WorkSpace, on_delete=models.CASCADE)


class Fix(models.Model):
    code = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    automobile = models.ForeignKey(Automobile, on_delete=models.CASCADE)
    workspace = models.ForeignKey(WorkSpace, on_delete=models.CASCADE)

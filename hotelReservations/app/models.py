from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Room(models.Model):
    number = models.IntegerField()
    num_beds = models.IntegerField()
    hasBalcony = models.BooleanField(default=False)
    isClean = models.BooleanField(default=False)


class Employee(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    description = models.TextField()
    POSITION_CHOICES = [
        ("Хигеничар", "Хигеничар"),
        ("Менаџер", "Менаџер"),
        ("Рецепционер", "Рецепционер"),
    ]
    job_position = models.CharField(choices=POSITION_CHOICES, max_length=50)
    start_year = models.IntegerField()


class Reservation(models.Model):
    name_surname = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    code = models.CharField(max_length=50, unique=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_photo = models.ImageField(upload_to='photos')
    isReserved = models.BooleanField(default=False)
    employer = models.ForeignKey(Employee, on_delete=models.CASCADE)


class EmployeeRoom(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

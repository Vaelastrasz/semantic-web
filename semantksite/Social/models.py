from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

class Photo(models.Model):
    url = models.CharField(max_length=255)
    photoname = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.photoname}'

class Person(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class Promotion(models.Model):
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    participants = models.ManyToManyField(Person)
    discount = models.IntegerField()
    name = models.CharField(max_length=255)
    winnersamount = models.IntegerField()
    def __str__(self):
        return f'{self.name}'

class Holiday(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.name}'

class Price(models.Model):
    amount = models.IntegerField()
    currency = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.name} {self.currency}'

class Event(models.Model):
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    subscribed = models.ManyToManyField(Person)
    likes = models.IntegerField()
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    eventname = models.CharField(max_length=255)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    holiday = models.ForeignKey(Holiday, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.eventname}'

class Location(models.Model):
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.city}'

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=20, choices=USER_ROLES, default='user', verbose_name='Role')
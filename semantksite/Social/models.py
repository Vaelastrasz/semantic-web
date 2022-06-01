from datetime import datetime
from django.db import models

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

class Event(models.Model):
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    subscribed = models.ManyToManyField(Person)
    likes = models.IntegerField()
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    eventname = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.eventname}'

class Location(models.Model):
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.city}'
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Location(models.Model):
    city_name = models.CharField(max_length=30)
    state_name = models.CharField(max_length=30)
    zip = models.CharField(max_length=6)
    lat = models.CharField(max_length=10)
    lng = models.CharField(max_length=10)

class Weather(models.Model):
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    wind = models.CharField(max_length=200)
    precipitation = models.FloatField()
    temperature = models.FloatField()
    weather = models.CharField(max_length=200)
    datetime = models.DateTimeField()

class Tweet(models.Model):
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    message = models.CharField(max_length=200)
    sentiment = models.FloatField()
    datetime = models.DateTimeField()
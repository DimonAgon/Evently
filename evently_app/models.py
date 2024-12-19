
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=900)
    description = models.TextField()
    datetime = models.DateTimeField()
    location = models.ForeignKey('Location', on_delete=models.PROTECT)
    organizer = models.ForeignKey('Organizer', on_delete=models.PROTECT)


class Location(models.Model):
    name = models.CharField(max_length=600)


class Organizer(models.Model):
    name = models.CharField(max_length=300)

from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=900)
    description = models.TextField()
    datetime = models.DateTimeField()
    location = models.ForeignKey('Location', on_delete=models.PROTECT)
    organizer = models.ForeignKey('Organizer', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Location(models.Model):
    name = models.CharField(max_length=600)

    def __str__(self):
        return self.name


class Organizer(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import User

#creation of first models of the app
class Flight(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure = models.DateTimeField()
    seats_available = models.PositiveIntegerField()

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rating=models.DecimalField(max_digits=2,decimal_places=1) #this field can be modified to be a choice field from 1 to 5

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    
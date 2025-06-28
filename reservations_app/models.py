from django.db import models
from django.contrib.auth.models import User

#stores fligth details
class Flight(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure = models.DateTimeField()
    seats_available = models.PositiveIntegerField()
    
#stores flight reservation details
class FlightReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(auto_now_add=True)
    # reservation_number=models.PositiveBigIntegerField(). future feature, reservation unique code

#Stores hotel information
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rating=models.DecimalField(max_digits=2,decimal_places=1) #this field can be modified to be a choice field from 1 to 5

#stores room hotel, represents info inside Hotel
class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE) #hotel room is related to Hotel, is deleted if hotel is deleted.
    room_number = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

#room reservation details
class RoomReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #booked room
    check_in = models.DateField()
    check_out = models.DateField() 
    reserved_at = models.DateTimeField(auto_now_add=True) #generates the timestamp when reserved





from django.db import models

# Create your models here.


class FlightsModel(models.Model):
    flightNumber =  models.CharField(max_length=30)
    departureAirport = models.CharField(max_length=3)
    arrivalAirport = models.CharField(max_length=3)
    departureDate = models.DateField()
    arrivalDate = models.DateField()

    class Meta:
        unique_together = ['flightNumber', 'departureDate']


class PassengersModel(models.Model):
    passengerId = models.CharField(max_length=30, primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    bookingId = models.CharField(max_length=6)
    email = models.CharField(max_length=30)
    flights = models.ManyToManyField(FlightsModel)



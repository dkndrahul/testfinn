from rest_framework.serializers import ModelSerializer
from passengers.models import PassengersModel, FlightsModel


class FlightSerializer(ModelSerializer):
    class Meta:
        model = FlightsModel
        exclude = ('id',)


class PassengerSerializer(ModelSerializer):
    flights = FlightSerializer(many=True)

    class Meta:
        model = PassengersModel
        fields = '__all__'


class AllPassengerList(ModelSerializer):
    class Meta:
        model = PassengersModel
        fields = ('passengerId', 'firstName', 'lastName', 'bookingId')



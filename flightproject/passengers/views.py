# Create your views here.
from rest_framework import viewsets, response
from passengers.models import PassengersModel, FlightsModel
from passengers.serializers import PassengerSerializer, AllPassengerList


class PassengerViewset(viewsets.ModelViewSet):
    queryset = PassengersModel.objects.all()
    serializer_class = PassengerSerializer

    def list(self, request, *args, **kwargs):
        flight_number = str(request.GET.get('flightNumber'))
        departure_date = request.GET.get('departureDate')
        flight_details = FlightsModel.objects.get(flightNumber=flight_number, departureDate=departure_date)
        all_passengers = PassengersModel.objects.filter(flights=flight_details)
        serializer = AllPassengerList(instance=all_passengers, many=True)
        return response.Response(serializer.data)
















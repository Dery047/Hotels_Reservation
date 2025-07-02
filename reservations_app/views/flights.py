from rest_framework import generics, permissions
from ..models import Flight, FlightReservation
from ..serializers import FlightSerializer, FlightReservationSerializer

class FlightListView(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [permissions.AllowAny]

class ReserveFlightView(generics.CreateAPIView):
    serializer_class = FlightReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
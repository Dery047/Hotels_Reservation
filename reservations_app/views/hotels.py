from rest_framework import generics, permissions
from ..models import Hotel, Room, RoomReservation
from ..serializers import HotelSerializer, RoomSerializer, RoomReservationSerializer

class HotelListView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.AllowAny]

class RoomListView(generics.ListAPIView):
    queryset = Room.objects.filter(available=True)
    serializer_class = RoomSerializer
    permission_classes = [permissions.AllowAny]

class ReserveRoomView(generics.CreateAPIView):
    serializer_class = RoomReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        room = serializer.validated_data['room']
        room.available = False
        room.save()
        serializer.save(user=self.request.user)

from django.urls import path
from .views import auth, flights, hotels

urlpatterns = [
    # Auth
    path('register/', auth.RegisterView.as_view(), name='register'),
    path('token/', auth.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', auth.TokenRefreshView.as_view(), name='token_refresh'),

    # Flights
    path('flights/', flights.FlightListView.as_view(), name='flight_list'),
    path('flights/reserve/', flights.ReserveFlightView.as_view(), name='reserve_flight'),

    # Hotels
    path('hotels/', hotels.HotelListView.as_view(), name='hotel_list'),
    path('rooms/', hotels.RoomListView.as_view(), name='room_list'),
    path('rooms/reserve/', hotels.ReserveRoomView.as_view(), name='reserve_room'),
]

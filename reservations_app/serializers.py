from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

# Serializer for User model (read-only password)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Model to serialize
        fields = ['id', 'username', 'email']  # Fields to include in serialization

# Serializer for registering new users
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Model to create
        fields = ['username', 'email', 'password']  # Fields expected on registration
        extra_kwargs = {'password': {'write_only': True}}  # Password won't be returned on GET

    # Override create to use Django's create_user (hashes password)
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

# Serializer for Flight model with all fields
class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'  # Include all fields from Flight model

# Serializer for FlightReservation model with all fields
class FlightReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightReservation
        fields = '__all__'  
# Serializer for Hotel model with all fields
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

# Serializer for Room model with all fields
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

# Serializer for RoomReservation model with all fields
class RoomReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomReservation
        fields = '__all__'

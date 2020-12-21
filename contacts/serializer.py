from rest_framework import serializers

from .models import Appointment, Social, MapMarker, Contacts


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'


class MapMarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapMarker
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'

from rest_framework import viewsets

from .models import Appointment, Social, MapMarker, Contacts
from .serializer import AppointmentSerializer, SocialSerializer, ContactsSerializer, MapMarkerSerializer


# class AppointmentView(viewsets.ModelViewset):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer


class SocialView(viewsets.ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer


class MapMarkerView(viewsets.ModelViewSet):
    queryset = MapMarker.objects.all()
    serializer_class = MapMarkerSerializer


class ContactsView(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

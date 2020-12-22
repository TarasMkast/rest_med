from rest_framework import viewsets, permissions

from .models import Appointment, Social, MapMarker, Contacts
from .serializer import AppointmentSerializer, SocialSerializer, ContactsSerializer, MapMarkerSerializer


# class AppointmentView(viewsets.ModelViewset):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer


class SocialView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Social.objects.all()
    serializer_class = SocialSerializer


class MapMarkerView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = MapMarker.objects.all()
    serializer_class = MapMarkerSerializer


class ContactsView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

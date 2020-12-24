from rest_framework import (
    viewsets,
    permissions,
)
from rest_framework.generics import RetrieveAPIView

from contacts.models import (
    Appointment,
    Social,
    MapMarker,
    Contacts,
)

from contacts.serializer import (
    AppointmentSerializer,
    SocialSerializer,
    ContactsSerializer,
    MapMarkerSerializer,
)


# class AppointmentView(viewsets.ModelViewset):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer


class SocialView(RetrieveAPIView, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Social.objects.all()
    serializer_class = SocialSerializer


class MapMarkerView(RetrieveAPIView, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = MapMarker.objects.all()
    serializer_class = MapMarkerSerializer


class ContactsView(RetrieveAPIView, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

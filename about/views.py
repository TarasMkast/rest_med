from .models import Clinic, Doctor, Gallery

from rest_framework import viewsets, permissions

from .serializer import ClinicSerializer, DoctorSerializer, GallerySerializer


class ClinicView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer


class DoctorView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class GalleryView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


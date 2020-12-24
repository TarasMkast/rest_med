from rest_framework import (
    viewsets,
    permissions,

)

from rest_framework.generics import (
    GenericAPIView,
    RetrieveAPIView,
)

from rest_framework.mixins import ListModelMixin

from about.models import (
    Clinic,
    Doctor,
    Gallery,
)

from about.serializer import (
    ClinicSerializer,
    DoctorSerializer,
    GallerySerializer,
)


class ClinicView(RetrieveAPIView, ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class DoctorView(RetrieveAPIView, ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class GalleryView(RetrieveAPIView, ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Gallery.objects.filter(is_active=True)
    serializer_class = GallerySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


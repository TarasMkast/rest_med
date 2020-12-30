from rest_framework import (
    viewsets,
    permissions,
)
from rest_framework.generics import RetrieveAPIView
from config.models import (
    LicenseField,
    Background,
)
from config.serializer import (
    LicenseFieldSerializer,
    BackgroundSerializer,
)


class BackgroundView(RetrieveAPIView, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer


class LicenseFieldView(RetrieveAPIView, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = LicenseField.objects.all()
    serializer_class = LicenseFieldSerializer


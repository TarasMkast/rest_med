from config.models import (LicenseField, Background)
from config.serializer import (LicenseFieldSerializer, BackgroundSerializer)
from rest_framework import (viewsets, permissions)


class BackgroundView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer


class LicenseFieldView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = LicenseField.objects.all()
    serializer_class = LicenseFieldSerializer


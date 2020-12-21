from .models import LicenseField, Background
from .serializer import LicenseFieldSerializer, BackgroundSerializer
from rest_framework import viewsets


class BackgroundView(viewsets.ModelViewSet):

    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer


class LicenseFieldView(viewsets.ModelViewSet):

    queryset = LicenseField.objects.all()
    serializer_class = LicenseFieldSerializer


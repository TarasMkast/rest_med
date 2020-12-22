from services.models import Services, ServiceItems
from rest_framework import viewsets, permissions
from .serializer import ServicesSerializer, ServicesItemsSerializer


class ServicesView(viewsets.ModelViewSet):
    # @TODO Fuck this shit
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ServicesItemsView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = ServiceItems.objects.all()
    serializer_class = ServicesItemsSerializer

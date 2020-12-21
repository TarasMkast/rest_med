from services.models import Services, ServiceItems
from rest_framework import viewsets
from .serializer import ServicesSerializer, ServicesItemsSerializer


class ServicesView(viewsets.ModelViewSet):

    # @TODO Fuck this shit
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ServicesItemsView(viewsets.ModelViewSet):
    queryset = ServiceItems.objects.all()
    serializer_class = ServicesItemsSerializer

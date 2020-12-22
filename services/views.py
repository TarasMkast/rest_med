from rest_framework import (
    viewsets,
    permissions,
)

from services.models import (
    Services,
    ServiceItems,
)

from services.serializer import (
    ServicesSerializer,
    ServicesItemsSerializer,
)


class ServicesView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ServicesItemsView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = ServiceItems.objects.all()
    serializer_class = ServicesItemsSerializer

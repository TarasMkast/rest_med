from rest_framework import (
    viewsets,
    permissions,
)
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import ListModelMixin

from services.models import (
    Services,
    ServiceItems,
)

from services.serializer import (
    ServicesSerializer,
    ServicesItemsSerializer,
)


class ServicesView(RetrieveAPIView, ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ServicesItemsView(RetrieveAPIView, ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = ServiceItems.objects.all()
    serializer_class = ServicesItemsSerializer


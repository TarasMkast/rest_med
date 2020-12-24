from rest_framework import (
    viewsets,
    permissions,
)
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import ListModelMixin

from news.models import News
from news.serializer import NewsSerializer


class NewsView(RetrieveAPIView, ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = News.objects.all()
    serializer_class = NewsSerializer


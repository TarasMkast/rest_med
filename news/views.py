from rest_framework import (viewsets, permissions)
from news.models import News
from news.serializer import NewsSerializer


class NewsView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = News.objects.all()
    serializer_class = NewsSerializer

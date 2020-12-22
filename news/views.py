from rest_framework import viewsets, permissions
from .models import News
from .serializer import NewsSerializer


class NewsView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = News.objects.all()
    serializer_class = NewsSerializer

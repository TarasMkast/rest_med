from rest_framework import viewsets
from .models import News
from .serializer import NewsSerializer


class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

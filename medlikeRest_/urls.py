from django.contrib import admin
from django.urls import path, include
from medlikeRest_.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('config.urls')),
    path('', include('about.urls')),
    path('', include('news.urls')),
    path('', include('contacts.urls')),
    path('', include('services.urls')),
    path('', include('about.urls')),
]
urlpatterns += doc_urls


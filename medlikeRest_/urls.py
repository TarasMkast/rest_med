
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('config.urls')),
    path('', include('about.urls')),
    path('', include('news.urls')),
    path('', include('contacts.urls')),
    path('', include('services.urls')),
    path('', include('about.urls')),
]


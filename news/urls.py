from django.urls import path
from .views import *

urlpatterns = [
    path('news/', NewsView.as_view({'get': 'list'})),
    path('news/<int:pk>', NewsView.as_view({'get': 'retrieve'}))
]

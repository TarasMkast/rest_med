from rest_framework import serializers
from .models import Services, ServiceItems


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class ServicesItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItems
        fields = '__all__'

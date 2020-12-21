from rest_framework import serializers

from .models import Background, LicenseField


class BackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Background
        fields = '__all__'


class LicenseFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenseField
        fields = '__all__'

from django.contrib import admin
from core.utils import CustomModelAdmin
from config.models import *


@admin.register(Background)
class BackgroundAdmin(CustomModelAdmin):
    fields = ('image', 'is_active')

    def has_add_permission(self, request):
        if not self.model.objects.count():
            return True
        return False

@admin.register(LicenseField)
class LicenseFieldAdmin(CustomModelAdmin):
    fields = ('license_field',)

    def has_add_permission(self, request):
        if not self.model.objects.count():
            return True
        return False

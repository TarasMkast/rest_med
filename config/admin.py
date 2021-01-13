from django.contrib import admin
from .models import *


@admin.register(Background)
class BackgroundAdmin(CustomModelAdmin):
    fields = ('image', 'is_active')

    def has_add_permission(self, request):
        if not self.model.objects.count():
            return True
        return False

@admin.register(LicenseField)
class LicenseFieldAdmin(admin.ModelAdmin):
    fields = ('license_field',)

    def has_add_permission(self, request):
        if not self.model.objects.count():
            return True
        return False

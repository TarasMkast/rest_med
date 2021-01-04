from django.contrib import admin
from core.utils import CustomModelAdmin
from config.models import *


@admin.register(Background)
class BackgroundAdmin(CustomModelAdmin):
    readonly_fields = ('background_photo',)
    fields = ('background_photo', 'image', 'is_active')


@admin.register(LicenseField)
class LicenseFieldAdmin(CustomModelAdmin):
    fields = ('license_field',)


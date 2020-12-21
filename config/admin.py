from django.contrib import admin
from .models import *


@admin.register(Background)
class BackgroundAdmin(admin.ModelAdmin):
    readonly_fields = ('background_photo',)
    fields = ('background_photo', 'image', 'is_active')


@admin.register(LicenseField)
class LicenseFieldAdmin(admin.ModelAdmin):
    fields = ('license_field',)

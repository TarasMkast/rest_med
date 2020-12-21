from django.contrib import admin
from .models import *


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    fields_display = ['name', 'phone', 'additional', 'created_date', 'status']


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    fields = ['name', 'url']


@admin.register(MapMarker)
class MapMarkerAdmin(admin.ModelAdmin):
    fields = ['latitude', 'longitude']


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    fields = ['address', 'email', 'first_phone', 'second_phone', 'schedule']

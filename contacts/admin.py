from django.contrib import admin
from contacts.models import *
from core.utils import CustomModelAdmin

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
class ContactsAdmin(CustomModelAdmin):
    fields = ['address', 'email', 'first_phone', 'second_phone', 'schedule']


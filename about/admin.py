from django.contrib import admin
from .models import *


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display_linked = ('title', 'description', 'doctor')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    fields = ('image', 'is_active', 'order', 'surname', 'name', 'second_name', 'description')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image', )

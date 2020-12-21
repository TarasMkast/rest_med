from django.contrib import admin
from services.models import Services, ServiceItems


class ServiceItemsAdmin(admin.ModelAdmin):
    list_display = ('services', 'description', 'price')


admin.site.register(Services)
admin.site.register(ServiceItems, ServiceItemsAdmin)

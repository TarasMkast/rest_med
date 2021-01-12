from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = ('image', 'title', 'text', 'is_active', 'order')

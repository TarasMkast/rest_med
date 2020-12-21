from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = ('news_image', 'image', 'title', 'text', 'is_active', 'order')
    readonly_fields = ('news_image',)

from django.utils.html import mark_safe
from django.db import models
from core.models import ActiveOrder


class Background(ActiveOrder, models.Model):
    image = models.ImageField(verbose_name="Фон на головній сторінці")

    class Meta:
        ordering = ['-is_active']
        verbose_name = "Фон"
        verbose_name_plural = "Фон"

    def __str__(self):
        return self.image.name

    def background_photo(self):
        if self.image:
            return mark_safe('<img src="/media/%s"/ style="width=500px; height: 500px">' % self.image)
        return 'Немає фотографії'

    background_photo.short_description = 'Фото'


class LicenseField(models.Model):
    license_field = models.CharField(max_length=255, verbose_name="Ліцензія")

    class Meta:
        verbose_name = "Ліцензія"
        verbose_name_plural = "Ліцензія"

from django.db import models
from core.models import TimeStamp
from django.utils.html import mark_safe
from core.models import ActiveOrder


class News(TimeStamp, ActiveOrder, models.Model):
    image = models.ImageField(verbose_name='Обрати фото')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Новина"
        verbose_name_plural = "Новини"

    def __str__(self):
        return self.title

    def news_image(self):
        if self.image:
            return mark_safe('<img src="/media/%s"/>' % self.image)
        return 'Немає фотографії'

    news_image.short_description = 'Фото'

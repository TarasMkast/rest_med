from django.utils.html import mark_safe
from django.db import models
from core.models import TimeStamp, ActiveOrder


class Clinic(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Опис')
    doctor = models.OneToOneField('Doctor', null=True, on_delete=models.SET_NULL, verbose_name='Головний лікар')

    class Meta:
        verbose_name = 'Про Клініку'
        verbose_name_plural = 'Про Клініку'

    def __str__(self):
        return "{}".format(self.title)


class Doctor(TimeStamp, ActiveOrder, models.Model):
    image = models.ImageField(verbose_name='Обрати фото')
    surname = models.CharField(max_length=255, verbose_name='Прізвище')
    name = models.CharField(max_length=255, verbose_name="Ім'я")
    second_name = models.CharField(max_length=255, verbose_name='По-батькові')
    description = models.TextField(verbose_name='Опис')

    class Meta:
        ordering = ['name', 'description']
        verbose_name = 'Лікар'
        verbose_name_plural = 'Лікарі'

    def __str__(self):
        return "{} {} {}".format(self.surname, self.name, self.second_name)

    def doctor_photo(self):
        if self.image:
            return mark_safe('<img src="/media/%s"/>' % self.image)
        return 'Немає фотографії'

    doctor_photo.short_description = 'Фото'


class Gallery(TimeStamp, ActiveOrder, models.Model):
    image = models.ImageField(verbose_name='Фото')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Галарея'

    def gallery_photo(self):
        if self.image:
            return mark_safe('<img src="/media/%s"/>' % self.image)
        return 'Немає фотографії'

    gallery_photo.short_description = 'Фото'

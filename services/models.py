from django.db import models
from core.models import TimeStamp, ActiveOrder


class Services(TimeStamp, ActiveOrder, models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=40, verbose_name='Послуга')
    description = models.TextField(verbose_name='Опис')

    class Meta:
        verbose_name = 'Послуга'
        verbose_name_plural = 'Послуги'
        ordering = ['order']

    def __str__(self):
        return self.title


class ServiceItems(TimeStamp, ActiveOrder, models.Model):
    services = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Послуга', related_name='RelServices')
    description = models.CharField(max_length=500, verbose_name='Опис')
    price = models.CharField(max_length=30, verbose_name='Ціна')

    class Meta:
        verbose_name = 'Опис послуги'
        verbose_name_plural = 'Опис послуг'
        ordering = ['services']

    def __str__(self):
        return self.description

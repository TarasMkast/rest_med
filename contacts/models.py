from django.db import models
from core.models import TimeStamp, ActiveOrder
from phone_field import PhoneField

CHOICES = [
    (True, 'Виконано'),
    (False, 'Очікує')
]


class Appointment(TimeStamp, ActiveOrder, models.Model):
    name = models.CharField(max_length=255, verbose_name="Ім'я")
    phone = PhoneField()
    additional = models.CharField(max_length=255, blank=True, default="")

    class Meta:
        ordering = ['-is_active', 'created_date']
        verbose_name = 'Запис на прийом'
        verbose_name_plural = "Записи на прийом"

    def __str__(self):
        return self.name, self.phone, self.additional


def status(self):
    if self.is_active:
        return "В процесі"
    return "Виконано"


def info(self):
    if self.additional == "":
        return "---"
    return self.additional


class Social(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    url = models.URLField(verbose_name="Посилання")

    class Meta:
        verbose_name = "Соціальну мережу"
        verbose_name_plural = "Соціальні мережі"

    def __str__(self):
        return self.name


class MapMarker(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        verbose_name = "ГеоДані"
        verbose_name_plural = "ГеоДані"

    def __str__(self):
        return "Маркер"


class Contacts(models.Model):
    address = models.CharField(max_length=255, verbose_name="Адреса")
    email = models.EmailField()
    first_phone = PhoneField()
    second_phone = PhoneField()
    schedule = models.TextField(verbose_name="Графік роботи")

    class Meta:
        verbose_name = "Котактні дані"
        verbose_name_plural = "Котактні дані"

    def __str__(self):
        return "Контакти"

from django.db import models


class TimeStamp(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ActiveOrder(models.Model):
    is_active = models.BooleanField(default=True)
    order = models.SmallIntegerField(default=1)

    class Meta:
        abstract = True

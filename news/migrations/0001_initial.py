# Generated by Django 3.1.4 on 2020-12-11 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('order', models.SmallIntegerField(default=1)),
                ('image', models.ImageField(upload_to='', verbose_name='Обрати фото')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Новина',
                'verbose_name_plural': 'Новини',
                'ordering': ['-created_date'],
            },
        ),
    ]

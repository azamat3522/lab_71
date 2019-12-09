# Generated by Django 2.2 on 2019-12-09 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=2000, verbose_name='Teкст цитаты')),
                ('author_name', models.CharField(max_length=30, verbose_name='Имя автора')),
                ('author_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('status', models.CharField(choices=[('new', 'Новая'), ('approved', 'Проверена')], default='new', max_length=20, verbose_name='Статус')),
                ('rating', models.IntegerField(default=0, verbose_name='Рэйтинг')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Цитаты',
            },
        ),
    ]

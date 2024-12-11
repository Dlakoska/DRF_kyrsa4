# Generated by Django 5.1.4 on 2024-12-11 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='telegram_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users/avatars/', verbose_name='Аватарка'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_subscribe',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Подписка на напоминания'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='Телефон'),
        ),
        migrations.AddField(
            model_name='user',
            name='tg_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Ваш Telegram_id'),
        ),
        migrations.AddField(
            model_name='user',
            name='tg_username',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ваш Telegram_name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Ваш E-mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ваше имя'),
        ),
    ]

# Generated by Django 2.2.6 on 2019-10-17 04:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('memoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='day',
            name='text',
            field=models.TextField(blank=True, verbose_name='memo'),
        ),
    ]
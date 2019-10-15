# Generated by Django 2.2.6 on 2019-10-15 07:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('text', models.TextField(verbose_name='main')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date')),
            ],
        ),
    ]

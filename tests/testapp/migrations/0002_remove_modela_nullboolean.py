# Generated by Django 2.2.10 on 2021-01-25 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modela',
            name='nullboolean',
        ),
    ]

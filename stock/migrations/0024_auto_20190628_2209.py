# Generated by Django 2.2 on 2019-06-28 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0023_auto_20190628_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticker',
            name='ticker',
            field=models.CharField(default='hi', max_length=10),
        ),
    ]
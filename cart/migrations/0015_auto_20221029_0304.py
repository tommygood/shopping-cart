# Generated by Django 3.2 on 2022-10-29 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_auto_20221029_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_cart',
            name='delivered',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='shop_cart',
            name='paid',
            field=models.IntegerField(default=1),
        ),
    ]
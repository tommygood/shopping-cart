# Generated by Django 3.2 on 2022-10-29 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0017_auto_20221029_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_cart',
            name='paid',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
# Generated by Django 3.2 on 2022-10-29 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20221029_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pwd',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
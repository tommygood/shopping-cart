# Generated by Django 3.2 on 2022-10-29 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_user_pwd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='no',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
    ]

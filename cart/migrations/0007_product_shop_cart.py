# Generated by Django 3.2 on 2022-10-29 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20221029_0221'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('no', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=15, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='shop_cart',
            fields=[
                ('no', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('uId', models.IntegerField(blank=True, null=True)),
                ('pId', models.IntegerField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('paid', models.IntegerField(blank=True, default=0, null=True)),
                ('delivered', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]

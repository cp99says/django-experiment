# Generated by Django 5.1.1 on 2024-11-09 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_restaurant_options_restaurant_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.menuitems')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.restaurant')),
            ],
        ),
    ]
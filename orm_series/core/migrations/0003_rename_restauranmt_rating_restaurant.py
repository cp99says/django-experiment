# Generated by Django 5.1.1 on 2024-09-29 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='restauranmt',
            new_name='restaurant',
        ),
    ]